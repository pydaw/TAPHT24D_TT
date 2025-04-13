from behave import given, when, then
from playwright.sync_api import Page, Locator, expect
from pages.add_friend_page import AddFriendPage
from pages.friend_page import FriendPage

@given(u'användaren befinner sig på vyn för att lägga till en vän')
def step_impl(context):
    add_friend_page = AddFriendPage(context.page)
    add_friend_page.navigate()
    

@when(u'sparar vän "My Friend" med epost "my@friend.se"')
def step_impl(context):
    add_friend_page = AddFriendPage(context.page)
    context.add_name = "My Friend"
    add_friend_page.add_name(context.add_name)
    context.add_email = "my@friend.se"
    add_friend_page.add_email(context.add_email)
    add_friend_page.click_save_button()


@then(u'kontrollera att ny kontaktuppgift finns i listan')
def step_impl(context):
    friend_page = FriendPage(context.page)
    friend_page.navigate()
    names = friend_page.get_friends_name()
    assert context.add_name in names
    emails = friend_page.get_friends_email()
    assert context.add_email in emails
    

@when(u'sparar vän "" med epost "my@friend.se"')
def step_impl(context):
    add_friend_page = AddFriendPage(context.page)
    context.add_name = ""
    add_friend_page.add_name(context.add_name)
    context.add_email = "my@friend.se"
    add_friend_page.add_email(context.add_email)
    

@when(u'sparar vän "My Friend" med epost ""')
def step_impl(context):
    add_friend_page = AddFriendPage(context.page)
    context.add_name = "My Friend"
    add_friend_page.add_name(context.add_name)
    context.add_email = ""
    add_friend_page.add_email(context.add_email)
    

@then(u'användaren får ett meddelande att alla fälte inte är ifyllda')
def step_impl(context):
    add_friend_page = AddFriendPage(context.page)
    expect(add_friend_page.error).to_be_visible()
    expect(add_friend_page.error).to_contain_text("Fyll i båda fälten")