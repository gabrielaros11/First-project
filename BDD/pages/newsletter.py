from selenium.webdriver.common.by import By

from pages.base_page import Base_Page


class Newsletter(Base_Page):
    def abonare_noutati(self):
        self.driver.get("https://carturesti.ro/")
        self.driver.find_element(By.XPATH, "//input[@id='mce-EMAIL']").send_keys("nume.prenume@yahoo.com")
        self.driver.find_element(By.CSS_SELECTOR, "[id='mce-FNAME']").send_keys("Popescu")
        self.driver.find_element(By.CSS_SELECTOR, "[id='mce-LNAME']").send_keys("Maria")
        self.driver.find_element(By.CSS_SELECTOR, "[id='mc-embedded-subscribe']").click()