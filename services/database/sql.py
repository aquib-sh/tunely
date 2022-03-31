import datetime
import sqlite3


class QueryGenerator:
    """Main work is to generate queries to be used by the controller."""

    def __init__(self):
        self.__table = "Themes"

    # setters
    def set_table_name(self, new_name: str):
        self.__table = new_name

    # getters
    def get_table_name(self) -> str:
        return self.__password_table

    def create_tbl(self):
        return f"""CREATE TABLE IF NOT EXISTS {self.__table}
            (
                THEME_DAY TEXT NOT NULL,
                THEME1 TEXT NOT NULL,
                THEME2 TEXT NOT NULL,
                VIDEO_LINK TEXT NOT NULL,
                TIMESTAMP TEXT NOT NULL
            );
            """

    def add_link(
        self, theme_day:str, theme1:str, theme2:str, video_link:str
    ) -> tuple:
        current_datetime = str(datetime.datetime.now())
        query = f"""INSERT INTO {self.__table} 
            (THEME_DAY, THEME1, THEME2, VIDEO_LINK, TIMESTAMP) 
            VALUES (?, ?, ?, ?, ?);"""
        params = (
            theme_day,
            theme1,
            theme2,
            video_link,
            current_datetime
        )
        return (query, params)

    def get_video_links(self, theme_day:str, theme1:str, theme2:str) -> tuple:
        query = f"""SELECT VIDEO_LINK FROM {self.__table} 
        WHERE THEME_DAY=:theme_day
        AND THEME1=:theme1
        AND THEME2=:theme2;"""
        params = {
            "theme_day": theme_day,
            "theme1": theme1,
            "theme2": theme2
        }
        return (query, params)

class QueryExecutor:
    def __init__(self, sqlite_file_path: str, log=1):
        self.conn = sqlite3.connect(sqlite_file_path)
        self.cursor = self.conn.cursor()
        self.log = log
        if self.log:
            print(f"[+] Connect to database at {sqlite_file_path}")

    def create_table(self, query):
        self.cursor.execute(query)
        self.conn.commit()

    def modify_data(self, query, params):
        self.cursor.execute(query, params)
        self.conn.commit()
    
    def theme_exists(self, query, params) -> bool:
        self.cursor.execute(query, params)
        fetched_links = self.cursor.fetchone()
        return (fetched_links != None)

    def get_all_links_for_theme(self, query, params) -> list:
        self.cursor.execute(query, params)
        fetched_links = self.cursor.fetchall()
        links = [row[-1] for row in fetched_links]
        return links
