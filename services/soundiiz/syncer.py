import time
import random

class SoundiizSyncer:
    def __init__(self, bot):
        self.bot = bot

    def load_page(self):
        self.bot.move("https://soundiiz.com/webapp/playlists")
        time.sleep(3)
        try:
            self.bot.get_element('//button[@title="Close"]').click()
        except:
            pass

    def sync(self, url: str):
        """Runs Syncronizer and Syncs the YouTube playlist to Spotify.
        
        Parameters
        ----------
        url: str
            YouTube Playlist URL
        """
        #================= CSS SELECTORS ==================
        sync_btn_sltr = '#app > div > section > div.navigation.for-desktop > div.navigation-inner > div.scroller.null > div > div.tools > div:nth-child(3) > span > button > div > div > span'
        playlist_url_btn_sltr = 'body > div.ReactModalPortal > div > div > div > div > div.flex-full.flex-row > div > div > div.autosizer-wrapper > div:nth-child(1) > div > div > div:nth-child(1) > div > div.selector-content > span'
        spotify_btn_sltr = 'div.platform-selector:nth-child(2)'
        new_playlist_sltr = 'div.list-selector:nth-child(1)'
        confirm_n_continue_btn = '.step-confirm > button:nth-child(1)'
        save_config_btn = '.step-confirm > button:nth-child(1)'
        run_now = '.schedule-starter'
        #================ XPATHS ==========================
        input_url_box = '//input[@type="url"]'
        confirm_btn = '//button[@type="submit"]'
        #confirm_n_continue_btn = '//button[@class="btn"]'        

        print(f"[+] Creating Sync for YouTube playlist: {url}")

        # Click on sync button from left panel
        self.bot.get_element_by_css_selector(sync_btn_sltr).click()
        time.sleep(random.random())

        # Click on enter playlist URL button
        self.bot.get_element_by_css_selector(playlist_url_btn_sltr).click()
        time.sleep(random.random())

        # Enter the YouTube URL into the box
        self.bot.get_element(input_url_box).send_keys(url)
        time.sleep(random.random())

        # Press Confirm to continue
        self.bot.get_element(confirm_btn).click()
        time.sleep(2.3)

        # Press Confirm and Continue
        self.bot.get_element_by_css_selector(confirm_n_continue_btn).click()
        time.sleep(2.5)

        # Press Spotify
        self.bot.get_element_by_css_selector(spotify_btn_sltr).click()
        time.sleep(random.random())
        
        # Press new playlist to create a new on
        self.bot.get_element_by_css_selector(new_playlist_sltr).click()
        time.sleep(3)

        # Press confirm and continue
        self.bot.get_element_by_css_selector(confirm_n_continue_btn).click()
        time.sleep(random.random())

        self.bot.get_element_by_css_selector(save_config_btn).click()
        print("[+] Saving all the configuration")
        time.sleep(3.56)

        self.bot.get_element_by_css_selector(run_now).click()
        print("[+] Synchronizing using Run Now")

    
    def execute_run_now(self, title: str, date: str, by_date=False):
        """Clicks on Run Now for a sync."""
        #================== XPATHS ========================
        my_syncs_list = '//div[@class="ReactVirtualized__Grid__innerScrollContainer"]/a'

        print("[+] Heading to MySyncs")
        
        self.bot.move('https://soundiiz.com/webapp/scheduleds')
        syncs_elems_list = self.bot.get_elements(my_syncs_list)
        needed = None

        if by_date:
            print(f"[+] Selecting sync for date {date}")
        else:
            print(f"[+] Selecting sync with title {title}")

        for elem in syncs_elems_list:
            if by_date:
                if date in elem.text:
                    needed = elem
                    needed.click()
                    break
            
            if elem.text == title:
                needed = elem
                needed.click()
                break
        
        if needed == None: print("[!] Unable to find the desired playlist");return
        
        print("[+] Executing Run Now...")
        time.sleep(2)
        self.bot.get_element_by_class('schedule-starter').click() #Perform run now
            