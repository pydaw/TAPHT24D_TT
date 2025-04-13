from behave import given, when, then
from playwright.sync_api import Page, Locator, expect
from pages.friend_page import FriendPage


def search_result(friend_page: FriendPage, search):
    # Search by mail
    if "@" in search:
        emails = friend_page.get_friends_email()
        result = len(emails) == 1 and (str(search).lower() in str(emails[0]).lower())

    # Search name
    else:
        names = friend_page.get_friends_name()
        result = len(names) == 1 and (str(search).lower() in str(names[0]).lower())

    return result


@when(u'skriver in "{search}" i sökfältet')
def step_impl(context, search):
    friend_page = FriendPage(context.page)
    friend_page.search(search)
    context.search_result = search_result(friend_page, search)


@when(u'skriver in "{search}" med gemener i sökfältet')
def step_impl(context, search):
    friend_page = FriendPage(context.page)
    friend_page.search(str(search).lower())
    context.search_result = search_result(friend_page, search)


@when(u'skriver in "{search}" med versaler i sökfältet')
def step_impl(context, search):
    friend_page = FriendPage(context.page)
    friend_page.search(str(search).upper())
    context.search_result = search_result(friend_page, search)


@then(u'skall listan visa "{number}" matchningar')
def step_impl(context, number):
    result = context.search_result
    assert bool(result)

    friend_page = FriendPage(context.page)
    assert friend_page.get_number_of_friends() == int(number)

