from .home_page import *
from .login_page import *
from .mine_page import *


class Page:

    def __init__(self, driver):
        self.driver = driver

    @property
    def login(self):
        return LoginPage(self.driver)

    @property
    def home(self):
        return HomePage(self.driver)

    @property
    def mine(self):
        return MinePage(self.driver)