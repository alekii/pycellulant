from typing import Dict

from pycellulant.cellulant.authenticator import Authenticator
from pycellulant.cellulant.cellulant_client import CellulantClient
from pycellulant.config.required_fields import RequiredApiFields
from pycellulant.validators.request_validator import RequestValidator


class CellulantService:
    """Handles Cellulant payment operations."""

    def __init__(self):
        self.authenticator = Authenticator()
        self.cellulant_client = CellulantClient()
        self.validator = RequestValidator()
        self.required_fields = RequiredApiFields()

    def checkout(self, checkout_request: Dict) -> Dict:
        self.validator.validate_payload(checkout_request, self.required_fields.checkout_request)
        self.cellulant_client.checkout(checkout_request)
