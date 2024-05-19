from selenium.webdriver.common.by import By

from BDD_examen.Pages.base_page import BasePage


class carturesti(BasePage):
    email = (By.CSS_SELECTOR, "[id='signupform-email']")
    parola = (By.CSS_SELECTOR, "[id='loginform-password']")
    autentificare = (By.CSS_SELECTOR, "[name='login-button']")
    def acces_to_carturesti(self):
        self.driver.find_element(*self.autentificare).click()
