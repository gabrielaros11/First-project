from behave import *
@when('I click on "{product_name}"')
def step_impl(context, product_name):
    context.search_page.click_searched_product(product_name)

