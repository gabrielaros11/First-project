from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pages.base_page import Base_Page


class Search_Page(Base_Page):
    def cautare_fotografie(self):
        self.driver.get("https://carturesti.ro/")
        self.driver.find_element(By.XPATH, "//input[@id='search-input']").send_keys("fotografie")
        self.driver.find_element(By.CSS_SELECTOR, "[placeholder='Căutare']").send_keys(Keys.ENTER)
    def pret_ascendent(self):
        self.driver.find_element(By.CSS_SELECTOR, "[id='select_option_46']")
        self.sort_by_price_element.value_of_css_property("Preț (ascendent)")
    def livrare_24h(self):
        self.driver.find_element(By.CSS_SELECTOR, "[class ='md-container md-ink-ripple']")
        #self.driver.find_element(By.CSS_SELECTOR, "[class='ng-binding ng-scope']").send_keys("Livrare 24h")

    def click_searched_product(self, product_name):
        self.driver.find_element(By.XPATH, f'//a[@title="{product_name}"]').click()


