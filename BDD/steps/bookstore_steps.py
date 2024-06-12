from behave import *
@when('When I click on HARTA - Carturesti Iulius Mall Cluj')
def step_impl(context):
    context.product_page.search_bookstore()