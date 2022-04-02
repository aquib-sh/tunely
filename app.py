import datetime

from services.service_manager import ServiceManager


class TuneloonsManager:
    def __init__(self, log=1):
        self.service_manager = ServiceManager()

    def frame_playlist_title(self, theme1, theme2) -> str:
        today = datetime.datetime.now()
        date = f"{today.year}-{today.month}-{today.day}"
        title = f"{date} {theme1} /{theme2}"
        return title

    def run(self):
        new_posted, info = self.service_manager.new_link_posted()

        # exit if new theme is not posted
        if (not new_posted): 
            return

        # Add the new theme data to DB and create a playlist as well
        theme_day = info[0]
        theme1 = info[1]
        theme2 = info[2]
        link = info[3]

        # Create a new playlist if it does not exist already
        title = self.frame_playlist_title(theme1, theme2)
        exists, _id = self.service_manager.playlist_exists(title)

        if (not exists):
            _id = self.service_manager.create_playlist(title)

        self.service_manager.add_to_playlist(playlist_id=_id, video_link=link)
        self.service_manager.add_record_to_db(theme_day, theme1, theme2, link)

if __name__ == "__main__":
    tmanager = TuneloonsManager()
    tmanager.run()
