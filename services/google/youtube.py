# Author: Shaikh Aquib
# Date  : Sept 2021

from services.google.google_services import GoogleServices

class YouTubeHandler(GoogleServices):
    """Handles the functions of YouTube using YouTube Data API.
    
    Parameters
    ----------
    token
        Token of the current session.

    scope: list
        Scope of the current token.
    """
    def __init__(self, token, scope: list):
        super().__init__(token, scope)

    def start_service(self, version: str):
        """Builds YouTube Data Service."""
        super().start_service("youtube", version)

