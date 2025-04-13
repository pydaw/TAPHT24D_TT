from behave import given, when, then
from playwright.sync_api import Page, Locator, expect
from pages.friend_page import FriendPage

@given(u'namn "Spock" är med i listan')
def step_impl(context):
    friend_page = FriendPage(context.page)
    friend = friend_page.get_friend("Spock")
    expect(friend).to_be_visible()
    context.number_of_friends = friend_page.get_number_of_friends()

@when(u'trycker på på "Ta bort" för namn')
def step_impl(context):
    friend_page = FriendPage(context.page)
    friend_page.remove_friend("Spock")    

@then(u'ska inte namnet finnas kvar i listan')
def step_impl(context):
    friend_page = FriendPage(context.page)
    friend = friend_page.get_friend("Spock")
    expect(friend).not_to_be_visible

    assert friend_page.get_number_of_friends() == context.number_of_friends - 1