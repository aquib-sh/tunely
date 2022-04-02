from services.database.sql import QueryExecutor, QueryGenerator


class DBManager:
    def __init__(self, db_path, log=1):
        self.query_exec = QueryExecutor(db_path)
        self.query_gen = QueryGenerator()
        self.log = log
        self.__setup()

    def __setup(self):
        self.query_exec.create_table(self.query_gen.create_tbl())

    def add_link(self, theme_day, theme1, theme2, video_link):
        query, param = self.query_gen.add_link(theme_day, theme1, theme2, video_link)
        self.query_exec.modify_data(query, param)
        if self.log: print(f"[+] ADDED {video_link} to {theme_day}_{theme1}_{theme2}")

    def theme_exists(self, theme_day, theme1, theme2) -> bool:
        query, param = self.query_gen.get_video_links(theme_day, theme1, theme2)
        status = self.query_exec.theme_exists(query, param)
        return status

    def link_exists(self, theme_day, theme1, theme2, link) -> bool:
        query, param = self.query_gen.get_video_links(theme_day, theme1, theme2)
        links = self.query_exec.get_all_links_for_theme(query, param)
        return (link in links)
