import config

from services.browser import BotMaker
from services.database.manager import DBManager
from services.facebook.group import FBGroup
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
        self.__db_manager = DBManager(config.db_path)
        self.__youtube = YouTubeCtl(gtoken, config.google_api_scope)
        self.__youtube.start_service()
        self.__browser = BotMaker(browser="Chrome", remote=True, port=8989)
        self.__facebook = FBGroup(self.__browser, config.fb_group_link)

    def get_fb(self):
        return self.__facebook

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

    def new_link_posted(self):
        self.__facebook.goto_announc()
        theme_day, theme1, theme2 = self.__facebook.get_todays_theme()
        link = self.__facebook.get_latest_video_link() 
        exists = self.__db_manager.link_exists(theme_day, theme1, theme2, link)
        if exists:
            return (False, ())
        else:
            return (True, (theme_day, theme1, theme2, link))

    def add_to_playlist(self, playlist_id:str, link:str):
        video_id = self.__get_video_id(link)
        self.__youtube.add_video_to_playlist(playlist_id, video_id)
        if self.log: print(f"[+] ADDED {link} to the playlist {playlist_id}")

    def playlist_exists(self, title) -> bool:
        playlists = self.__get_playlists()
        return (title in playlists)

    def create_playlist(self, title) -> str:
        resp = self.__youtube.create_playlist(title)
        if self.log: print(f"[+] CREATED {title} playlist")
        return resp['id']

    def delete_playlist(self, _id):
        self.__youtube.delete_playlist(playlist_id=_id)
        if self.log: print(f"[+] DELETED {_id} playlist")
