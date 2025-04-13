from behave import given, when, then

@given(u'användaren befinner sig på vyn för att lägga till en vän')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given användaren befinner sig på vyn för att lägga till en vän')


@when(u'sparar vän "My Friend" med epost "my@friend.se"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When sparar vän "My Friend" med epost "my@friend.se"')


@then(u'kontrollera att ny kontaktuppgift finns i listan')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then kontrollera att ny kontaktuppgift finns i listan')


@when(u'sparar vän "" med epost "my@friend.se"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When sparar vän "" med epost "my@friend.se"')


@then(u'användaren får ett meddelande att alla fälte inte är ifyllda')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then användaren får ett meddelande att alla fälte inte är ifyllda')


@when(u'sparar vän "My Friend" med epost ""')
def step_impl(context):
    raise NotImplementedError(u'STEP: When sparar vän "My Friend" med epost ""')