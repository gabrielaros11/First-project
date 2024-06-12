from selenium.webdriver.common.by import By

from pages.base_page import Base_Page


class Bookstore_Page(Base_Page):
    SEARCH_BOOKSTORE = (By.LINK_TEXT, "Librării")
    def iulius_mall(self):
        self.driver.find_element(By.CSS_SELECTOR, "[data-coordinates-lng='23.628259']")
    def verona(self):
        self.driver.find_element(By.LINK_TEXT, "https://www.instagram.com/carturesti_verona").click()
