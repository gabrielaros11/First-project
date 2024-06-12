import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pages.base_page import Base_Page


class Home_Page(Base_Page):

    def navigate_carturesti(self):
        self.driver.get("https://carturesti.ro/")
        self.driver.maximize_window()
        self.driver.find_element(By.CSS_SELECTOR, "[aria-label='allow cookies']").click()

    #def click_search_input(self):
    def input_product(self, product_name):
        self.driver.find_element(By.XPATH, "//input[@id='search-input']").send_keys(product_name)
        self.driver.find_element(By.CSS_SELECTOR, "[placeholder='Căutare']").send_keys(Keys.ENTER)
       # self.driver.find_element(By.CSS_SELECTOR, "[title='Revista Matca. Nr. 1']")
        #self.driver.find_element(By.CSS_SELECTOR, "[title='Adaugă în coș']")
    def access_bookstore(self, libraries_name):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "/librarii").click(libraries_name)
    def navigate_to_login(self):
        time.sleep(10)
        self.driver.find_element(By.XPATH, '//div[@class="meniu-dreapta clear-a"]//div[@class="_md md-open-menu-container md-whiteframe-z2"]//button').click()


