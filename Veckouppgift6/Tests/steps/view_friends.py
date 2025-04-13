from behave import given, when, then
from playwright.sync_api import Page
from pages.friend_page import FriendPage

@given(u'användaren befinner sig på sidan med vänlistan')
def step_impl(context):
    friend_page = FriendPage(context.page)
    friend_page.navigate()

@when(u'användaren tittar på listan')
def step_impl(context):
    friend_page = FriendPage(context.page)
    context.number_of_friends = friend_page.get_number_of_friends()

@then(u'användaren ser en lista med 5 vänner')
def step_impl(context):
    assert context.number_of_friends == 5
    