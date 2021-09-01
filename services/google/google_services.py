from googleapiclient.discovery import build

class GoogleServices:
    """Handles Google API events and methods.
    
    Parameters
    ----------
    token
        Token of the current session.

    scope: list
        Scope of the current token.
    """
    def __init__(self, token, scope: list):
        self.token = token
        self.scope = scope
        self.service = None

    def start_service(self, service: str, version: str):
        """Starts Google API Service.
        
        Parameters
        ----------
        service: str
            name of the service (example: calender, sheet, etc)

        version: str
            version of the service (example: v3)
        """
        self.service = build(service, version, credentials=self.token)
        return self.service