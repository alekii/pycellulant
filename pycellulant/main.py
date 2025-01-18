from pycellulant.cellulant.cellulant_client import HttpClient
from pycellulant.cellulant.authenticator import Authenticator
from pycellulant.cellulant.cellulant_service import CellulantService
if __name__ == "__main__":
    base_url = "https://sandbox.safaricom.co.ke"
    client_key = "your_client_key"
    client_secret = "your_client_secret"

    cellulant_service = CellulantService()

    response = mpesa_service.checkout(short_code="600123", amount=1000, phone_number="254700000000")
    print(response)
