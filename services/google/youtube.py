# Author: Shaikh Aquib
# Date  : Sept 2021

from services.google.google_services import GoogleServices

class YouTubeCtl(GoogleServices):
    """ YouTube Controller Class
    
    Controls the functions of YouTube using YouTube Data API.
    
    Parameters
    ----------
    token
        Token of the current session.

    scope: list
        Scope of the current token.

    Methods
    -------
    start_service(version: str)
        builds the service by calling start_service from
        super class and passing the parameters for YouTube service.
        returns a service object.

    """
    def __init__(self, token, scope: list):
        super().__init__(token, scope)

    def start_service(self, version: str):
        """Builds YouTube Data Service."""
        super().start_service("youtube", version)

