from playwright.sync_api import Page, Locator
from config.global_settings import BASE_URL

class AddFriendPage():
    def __init__(self, page: Page):
        self.page = page
        self.name_field = self.page.get_by_role("textbox").nth(0)
        self.email_field = self.page.get_by_role("textbox").nth(1)
        self.save_button = self.page.get_by_role("button", name="Spara")
        self.error = self.page.locator("p.error")
        
    def navigate(self):
        self.page.goto(BASE_URL+"add")

    def click_save_button(self):
        self.save_button.click()

    def add_name(self, name):
        self.name_field.fill(name)
    
    def add_email(self, email):
        self.email_field.fill(email)