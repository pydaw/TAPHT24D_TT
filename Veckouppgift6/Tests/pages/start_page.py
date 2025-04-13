from playwright.sync_api import Page
from config.global_settings import BASE_URL

class StartPage():
    def __init__(self, page: Page):
        self.page = page
        self.friends = self.page.locator(".friend")

    def navigate(self):
        self.page.goto(BASE_URL)