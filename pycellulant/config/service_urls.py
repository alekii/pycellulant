class ServiceUrls:
    """
    A class to manage service URLs for different environments
    (e.g., Production, Development, Testing).
    """

    def __init__(self, environment: str = "production") -> None:
        """
        Initialize the ServiceUrls class with the specified environment.

        :param environment: The environment to use ("production", "development", etc.).
        """
        if environment == "production":
            self.urls = Production()
        elif environment == "sandbox":
            self.urls = Sandbox()
        else:
            raise ValueError(f"Unsupported environment: {environment}")

    @property
    def checkout_url(self) -> str:
        """
        Return the checkout URL based on the environment.

        :return: The checkout URL.
        """
        return self.urls.checkout_url

    def __str__(self) -> str:
        return str(self.urls)

    def __repr__(self) -> str:
        return repr(self.urls)

class Sandbox:
    def __init__(self) -> None:
        self.base_url = "https://api-dev.tingg.africa/v3"
        self.checkout_url = f"{self.base_url}/checkout-api/checkout/request"

    def __str__(self) -> str:
        return '<Using Sandbox Urls>'

    def __repr__(self) -> str:
        return '<Using Sandbox Urls>'


class Production:
    pass
