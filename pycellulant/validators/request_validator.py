from typing import Dict, Set

class RequestValidator:

    @staticmethod
    def validate_payload(payload: Dict, required_fields: Set) -> bool:
        missing_fields = required_fields.difference(set(payload.keys()))
        if missing_fields:
            raise ValueError(f"Missing required fields: {', '.join(missing_fields)}")
        return True
