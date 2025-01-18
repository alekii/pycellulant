from pycellulant.cellulant.cellulant_client import HttpClient

class Authenticator:
    def __init__(self):
        self.http_client = HttpClient()

    def authenticated(self, func):
        def wrapper(self, *args, **kwargs):
            if not self.is_authenticated():
                raise PermissionError("User is not authenticated")
            return func(self, *args, **kwargs)

        return wrapper

