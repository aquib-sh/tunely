import sys
from soundiiz.login import SoundiizLogin
from soundiiz.syncer import SoundiizSyncer
from cache_memory import CacheProcessor

class SyncManager:
    def __init__(self):
        self.cache = CacheProcessor(basefile="themes.db", table="themes")

    def retrieve_data(self, date: str):
        """Returns the data from the database of the given date.
        
        Parameters
        ----------
        date: str
            date in yyyy-mm-dd format.
        """
        trimmed_data = []
        cache_data = self.cache.retrieve_cache()
        for cache in cache_data:
            #cache[0] is date
            if cache[0] == date:
                trimmed_data.append(cache)
        return trimmed_data
        
        