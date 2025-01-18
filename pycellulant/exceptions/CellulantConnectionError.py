class CellulantConnectionError(Exception):
    """This is exception will be thrown where there is no or slow internet connection
    """

    error_message = f"""

    Transaction couldn\'t be processed due to connection timeout
    Please make sure you have a stable internet Connection 
    """

    def __init__(self, error_message=error_message):
        super().__init__(error_message)
