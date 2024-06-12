from selenium.webdriver.common.by import By

from pages.base_page import Base_Page


class Product_page(Base_Page):
    ADD_TO_CART = (By.LINK_TEXT, "Adaugă în coș")
    def add_to_cart(self):
        self.driver.find_element(*self.ADD_TO_CART).click()
