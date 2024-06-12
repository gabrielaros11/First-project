from behave import *

@given(u'I am on the home page')
def step_impl(context):
    context.home_page.navigate_carturesti()



#@when('I click on search bar')
#def step_impl(context):
#    context.home_page



@when(u'I input my email')
def step_impl(context):
    (u'STEP: When I input my email')


@when(u'I input my password')
def step_impl(context):
    (u'STEP: When I input my password')

@then(u'I should be signed in to my account')
def step_impl(context):
    (u'STEP: Then I should be signed in to my account')


@when(u'I input a wrong password')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I input a wrong password')


@when(u'I click on AUTENTIFICARE button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click on AUTENTIFICARE button')


@then(u'I should get an error message')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should get an error message')