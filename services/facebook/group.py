import json
import os
import re
import time

from bs4 import BeautifulSoup


class FBGroup:
    """Interacts with Facebook group.
    
    Parameters
    ----------
    bot: bot.BotMaker
        BotMaker object of the browser.

    link: str
        Link of the Facebook group.

    """
    def __init__(self, bot, group_link):
        self.bot  = bot
        self.link = group_link
        self.theme_dir = "cache"
        if self.theme_dir not in os.listdir() : os.mkdir(self.theme_dir)
        self.theme_file = "themes.json"
        self.youtube_links_file = "links.json"
        self.theme_records = os.path.join(self.theme_dir, self.theme_file)
        self.youtube_link_records  = os.path.join(self.theme_dir, self.youtube_links_file)

    def load_page(self):
        self.bot.move(self.link)
        time.sleep(3)
    
    def goto_announc(self):
        self.bot.move(self.link+"?view=announcements")

    def save_theme(self, title:str, themes:list):
        """Writes the given theme with title to a JSON file."""
        with open(self.theme_records, "w") as fp:
            json.dump({title:themes}, fp)

    def previous_theme(self) -> tuple:
        """Returns the theme saved previously."""
        if not os.path.exists(self.theme_records): return (None, None)
        with open(self.theme_records, "r") as fp:
            data = json.load(fp)
        if len(data) > 0:
            title, themes = tuple(data.items())[0]
            print(f"previous themes: {themes}")
            return (title.strip(), themes)
        return (None, None)

    def save_ytlink(self, link:str):
        """Writes the given YouTube video link to a JSON file."""
        with open(self.youtube_link_records, "w") as fp:
            json.dump({"youtube_link":link}, fp)

    def previous_ytlink(self) -> str:
        """Returns the YouTube video link saved previously."""
        if not os.path.exists(self.youtube_link_records): return None
        with open(self.youtube_link_records, "r") as fp:
            data = json.load(fp)
        if len(data) > 0: return data['youtube_link'].strip()
        return None

    def get_todays_theme(self) -> tuple:
        soup = BeautifulSoup(self.bot.page_source(), "lxml")
        pattern = r"([a-zA-Z]*\s(?:T|t)hemes):\s*\d(?:\.|\))\s?([a-zA-Z\s!]*)\d(?:\.|\))\s?([a-zA-Z\s]*)"
        latest_theme_info = soup.find("span", {"data-sigil":"more"}).text
        info = []
        themes = []
        title = ''
        match = re.search(pattern, latest_theme_info)
        if match == None:
            base = soup.find("span", {"data-sigil":"more"})
            title = base.find("div").find("div").text.strip(":").strip()
            themes = [theme.text.strip() for theme in base.find_all("li")]
        else:
            info = match.groups()
            if info == None or len(info) < 2 : return (None, None)
            title  = info[0]
            themes = info[1:]
        print(title, themes)
        return (title, themes)

    def get_latest_video_link(self) -> str:
        """Returns the latest YouTube video link.
        
        Returns
        -------
        :str
            video link from the latest post.
        """
        soup = BeautifulSoup(self.bot.page_source(), 'lxml')

        youtube_video = soup.find("a", {"class":"touchable", "target":"_blank"})['href']

        self.bot.move(youtube_video)
        video_link = self.bot.driver.current_url
        self.bot.driver.back() # Now goback to group page.
        return video_link
