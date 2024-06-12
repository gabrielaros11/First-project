from selenium.webdriver.common.by import By

from pages.base_page import Base_Page


class Retur(Base_Page):
    def retur(self):
        self.driver.get("https://carturesti.ro/")
        self.driver.find_element(By.CSS_SELECTOR, "[href='/info/politica-confidentialitate']").click()