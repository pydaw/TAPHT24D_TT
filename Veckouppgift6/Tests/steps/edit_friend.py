from behave import given, when, then
from playwright.sync_api import Page, Locator, expect
from pages.friend_page import FriendPage


@given(u'användaren befinner sig på vyn för att ändra en vän')
def step_impl(context):
    friend_page = FriendPage(context.page)
    friend_page.navigate()
    friend_page.click_edit_friend()


@when(u'spara namnet "batman"')
def step_impl(context):
    friend_page = FriendPage(context.page)
    name = "batman"
    context.edit_change = {"change_type": "name", "change": name}
    friend_page.edit_name(name)
    friend_page.click_save_button()


@when(u'spara epost "batman@cave.nu"')
def step_impl(context):
    friend_page = FriendPage(context.page)
    email = "batman@cave.nu"
    context.edit_change = {"change_type": "email", "change": email}
    friend_page.edit_email(email)
    friend_page.click_save_button()


@then(u'kontrollera att ändrad kontaktuppgift finns i listan')
def step_impl(context):
    friend_page = FriendPage(context.page)
    friend_page.get_friends_name()
    
    if context.edit_change["change_type"] == "name":
        friends_name = friend_page.get_friends_name()
        assert friends_name[0] == context.edit_change["change"]
    else:
        friends_email = friend_page.get_friends_email()
        assert friends_email[0] == context.edit_change["change"]


@when(u'spara namnet ""')
def step_impl(context):
    friend_page = FriendPage(context.page)
    name = ""
    friend_page.edit_name(name)


@when(u'spara epost ""')
def step_impl(context):
    friend_page = FriendPage(context.page)
    email = ""
    friend_page.edit_email(email)
    

@then(u'kontrollera att felmeddelande fås')
def step_impl(context):
    friend_page = FriendPage(context.page)
    expect(friend_page.edit_error).to_be_visible()
    expect(friend_page.edit_error).to_contain_text("Fyll i båda fälten")