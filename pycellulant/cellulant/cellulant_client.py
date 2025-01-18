from typing import Dict, Optional

import requests

from pycellulant.config.service_urls import ServiceUrls
from pycellulant.exceptions.CellulantConnectionError import CellulantConnectionError


class CellulantClient:
    def __init__(self,
        environment: Optional[str] = "sandbox") -> None:
        self.environment = environment
        self.urls = ServiceUrls(environment)

    def checkout(self, checkout_request: Dict) -> Dict:
        """
           Make a checkout request.

           :param checkout_request: The request payload for checkout.
           :return: The API response as a dictionary.
           """
        try:
            return requests.post(
                self.urls.checkout_url,
                json=checkout_request,
                headers=self.default_headers(),
                verify=True,
            ).json()

        except (requests.ConnectTimeout, requests.ConnectionError):
            raise CellulantConnectionError


    def default_headers(self, auth_key: Optional[str] = "") -> Dict:
        """Generate Default header to be used during a Request.
        """
        if not auth_key:
            auth_key = self.__generate_encrypted_key(session=True)
        return {
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(auth_key),
            "Origin": self.origin_address,
        }
