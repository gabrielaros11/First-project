from behave import *
@given(u'I am on Login page')
def step_impl(context):
    context.home_page.navigate_to_login()

@when('I click on the Utilizator Existent')
def step_impl(context):
    context.product_page.login()