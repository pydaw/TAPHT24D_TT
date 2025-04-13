from playwright.sync_api import Page, Locator
from config.global_settings import BASE_URL
import logging

class FriendPage():
    def __init__(self, page: Page):
        self.page = page
        self.friends = self.page.locator(".friend")
        self.search_field = self.page.get_by_placeholder("Sök namn")
        self.edit_button = self.page.get_by_role(role="button", name="Ändra")
        self.edit_name_field = self.page.get_by_role("textbox").nth(0)
        self.edit_email_field = self.page.get_by_role("textbox").nth(1)
        self.edit_save_button = self.page.get_by_role("button", name="Spara")
        self.edit_error = self.page.locator("p.error")
        
    def navigate(self):
        self.page.goto(BASE_URL+"friends")
        
    def get_number_of_friends(self):
        return self.friends.count()
    
    def get_friend(self, name):
        first: Locator = self.friends.get_by_text(name).first
        friend = first.locator('xpath=..')
        return friend
    
    def get_friends_name(self):
        names = []
        number_of_friends = self.get_number_of_friends()
        for i in range(number_of_friends):
            friend: Locator = self.friends.nth(i)
            name = friend.locator("div").nth(0).text_content().strip()
            names.append(name)
        return names

    def get_friends_email(self):
        email_accounts = []
        number_of_friends = self.get_number_of_friends()
        for i in range(number_of_friends):
            friend: Locator = self.friends.nth(i)
            email = friend.locator("div").nth(1).text_content().strip()
            email_accounts.append(email)
        return email_accounts

    def remove_friend(self, name):
        friend = self.get_friend(name)
        friend.get_by_text("Ta bort").click()
    
    def search(self, text):
        self.search_field.fill(text)

    def click_edit_friend(self):
        self.edit_button.nth(0).click()

    def click_save_button(self):
        self.edit_save_button.click()

    def edit_name(self, name):
        self.edit_name_field.fill(name)
    
    def edit_email(self, email):
        self.edit_email_field.fill(email)
    