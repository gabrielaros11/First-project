from selenium.webdriver.common.by import By

from pages.base_page import Base_Page


class Checkout(Base_Page):
    def empty_cart(self):
        self.driver.get("https://carturesti.ro/")
        self.driver.find_element(By.CSS_SELECTOR, "[class='checkout__text']").click()
    def add(self):
        self.driver.get("https://carturesti.ro/checkout")
        self.driver.find_element(By.XPATH, "//input[@id='product-2148909063-quantity']").send_keys("3")