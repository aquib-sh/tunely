import config

from services.google.token import TokenRetriever
from services.google.youtube import YouTubeCtl


class ServiceManager:
    """Manages different services and connects them."""
    def __init__(self, log=1):
        self.log = log
        token_retr = TokenRetriever()
        gtoken = token_retr.retrieve_google_api_token(
            config.google_api_token_path, config.google_api_scope
        )
        self.__youtube = YouTubeCtl(gtoken, config.google_api_scope)
        self.__youtube.start_service()

    def __get_playlists(self):
        return self.__youtube.fetch_playlists_title(
            config.youtube_channel_id, max_results=50
        )

    def __get_video_id(self, link):
        video_id = ""
        if link.startswith("https://youtu.be"):
            video_id = link.split(r"/")[1]
        elif link.startswith("https://www.youtube.com"):
            video_id = link.split(r"=")[1]
        return video_id

    def add_to_playlist(self, playlist_id:str, link:str):
        video_id = self.__get_video_id(link)
        self.__youtube.add_video_to_playlist(playlist_id, video_id)
        if self.log: print(f"[+] Added {link} to the playlist {playlist_id}")

    def search_in_playlist(self, title) -> bool:
        playlists = self.__get_playlists()
        return (title in playlists)

    def create_playlist(self, title) -> str:
        resp = self.__youtube.create_playlist(title)
        if self.log: print(f"[+] Sucessfully CREATED {title} playlist")
        return resp['id']

    def delete_playlist(self, _id):
        self.__youtube.delete_playlist(playlist_id=_id)
        if self.log: print(f"[+] Sucessfully DELETED {_id} playlist")


