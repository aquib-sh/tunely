class FBLogin:
    """Facebook Login page"""
    def __init__(self, bot):
        self.bot = bot
        self.url = "https://www.facebook.com/login"

    def load_page(self):
        """Loads the login page."""
        self.bot.move(self.url)

    def login(self, email:str, password:str):
        """Logs into Facebook account using the credentials provided.
        
        Parameters
        ----------
        email: str
            email address to use for login.

        password: str
            password to use for login.

        """
        email_box = self.bot.get_element('//input[@id="email"]')
        pswd_box  = self.bot.get_element('//input[@id="pass"]')
        login_btn = self.bot.get_element('//button[@id="loginbutton"]')

        email_box.clear()
        pswd_box.clear()

        email_box.send_keys(email)
        pswd_box.send_keys(password)
        login_btn.click()
    
