from selenium.webdriver.common.by import By

from pages.base_page import Base_Page


class Login_Page(Base_Page):
    def connected_successfully(self):
        self.driver.find_element(By.CSS_SELECTOR, "[id = 'modalLoginForm']")
        self.driver.find_element(By.XPATH, "//id[@'loginTrigger']").click()
        self.driver.find_element(By.ID, 'signupform-email').send_keys("nume.prenume@yahoo.com")
        self.driver.find_element(By.ID, "loginform-password").send_keys("Parola.1234")
        self.driver.find_element(By.CSS_SELECTOR, "[name='login-button']").click()
    def login_failed(self):
        self.driver.find_element(By.CSS_SELECTOR, "[id = 'modalLoginForm']")
        self.driver.find_element(By.XPATH, "//id[@'loginTrigger']").click()
        self.driver.find_element(By.ID, 'signupform-email').send_keys("nume.prenume@yahoo.com")
        self.driver.find_element(By.ID, "loginform-password").send_keys("parola.gresita")
        self.driver.find_element(By.CSS_SELECTOR, "[name='login-button']").click()