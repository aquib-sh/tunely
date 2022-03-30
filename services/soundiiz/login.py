import time
import random

class SoundiizLogin:
    """Logs into Soundizz account.
    
    Parameters
    ----------
    bot: bot.BotMaker
        BotMaker object with the browser initiated.
    """
    def __init__(self, bot):
        self.bot = bot
        self.url = "https://soundiiz.com/login"

    def load_page(self):
        self.bot.move(self.url)

    def login(self, username: str, password: str):
        """Logs into Soundizz account using the credentials provided.
        
        Parameters
        ----------
        username: str
            username to use for login.

        password: str
            password to use for login.

        """
        for char in username:
            self.bot.get_element('//input[@id="username"]').send_keys(char)
            time.sleep(random.random())

        for char in password:
            self.bot.get_element('//input[@id="password"]').send_keys(char)
            time.sleep(random.random())

        time.sleep(random.random())
        self.bot.get_element('//button[@id="_submit"]').click()

        