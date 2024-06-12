from browser import Browser
from pages.bookstore_page import Bookstore_Page
from pages.carturesti import Carturesti
from pages.home_page import Home_Page
from pages.login_page import Login_Page
from pages.product_page import Product_page
from pages.search_page import Search_Page


def before_all(context):
    context.browser = Browser()
    context.home_page = Home_Page()
    context.search_page = Search_Page()
    context.product_page = Product_page()
    context.bookstore_page = Bookstore_Page()
    context.login_page = Login_Page()

def after_all(context):
    context.browser.close()