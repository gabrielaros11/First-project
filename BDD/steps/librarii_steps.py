from behave import *

@given(u'I am on Librării page')
def step_impl(context):
    context.home_page.access_bookstore()