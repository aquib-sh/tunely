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
        """Builds YouTube Data Service.
        
        Parameters
        ----------
        version: str
            version of the YouTube Data API (example: v3)
        """
        super().start_service("youtube", version)


    def fetch_playlists(self, channel_id: str, max_results: int) -> dict:
        """Returns the JSON data on the list of playlists
           for a channel. 

        Parameters
        ----------
        channel_id: str
            id of channel where you want to get playlists from.
            this channel id can be found in the channel link
            example: https://www.youtube.com/channel/UC_aEa8K-EOJ3D6gOs7HcyNg
            here UC_aEa8K-EOJ3D6gOs7HcyNg is the channel_id

        max_results: int
            max results to return as JSON 
            ( if set to 2 then 2 playlists data will return)
            (acceptable values are between 0 to 50)
        """
        request = self.service.playlists().list(
            part="id, snippet,contentDetails", 
            channelId=channel_id, 
            maxResults=max_results
        )
        response = request.execute()

        return response

    
    def fetch_playlists_title(self, channel_id: str, max_results: int) -> list:
        """Returns the list containing titles of playlists 
           for a particular YouTube channel.

        Parameters
        ----------
        channel_id: str
            id of channel where you want to get playlists from.
            this channel id can be found in the channel link
            example: https://www.youtube.com/channel/UC_aEa8K-EOJ3D6gOs7HcyNg
            here UC_aEa8K-EOJ3D6gOs7HcyNg is the channel_id

        max_results: int
            max results to return as JSON 
            ( if set to 2 then 2 playlists data will return)
            (acceptable values are between 0 to 50)
        """
        response = self.fetch_playlists(channel_id, max_results)
        titles = []
        total_items = len(response['items'])

        for i in range(0, total_items):
            title = response['items'][i]['snippet']['title']
            titles.append(title)

        return titles