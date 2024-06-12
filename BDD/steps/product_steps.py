from behave import *
@when('I click on Adauga in cos')
def step_impl(context):
    context.product_page.add_to_cart()