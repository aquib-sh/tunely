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
        
        
    def create_playlist(
            self, 
            title: str, 
            description: str = None, 
            status: str = "public") -> dict:
        """Creates a new playlist on YouTube channel.
        
        Parameters
        ----------
        title: str
            title fo the new playlist to be created.

        description: str (OPTIONAL, DEFAULT=None)
            description of the playlist.

        status: str (OPTIONAL, DEFAULT='public')
            privacy setting of the playlist

            if set to 'public' anyone can 
            access the playlist and can be
            showed in YouTube search results.

            if set to 'private' only you can 
            access the playlist.

            if set to 'unlisted' anyone with a link
            can access the playlist, but won't turn up
            in search results.

        Returns
        -------
        response: dict
            response generated after the execution of request
            
        """
        # Throw error if user entered wrong status 
        accepted_status = ['public', 'private', 'unlisted']
        if status not in accepted_status:
            raise Exception("Invalid Status", 
                f"status shoud be in {accepted_status}") 

        request = self.service.playlists().insert(
            part="id, snippet, status, contentDetails",
            body={
                "snippet": {
                    "title": title,
                    "description":description,
                },
                "status": {
                    "privacyStatus": status
                }
           } 
        )
        response = request.execute()
        return response
        
        
