from selenium.webdriver.common.by import By


class Carturesti():
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
    def empty_cart(self):
        self.driver.get("https://carturesti.ro/")
        self.driver.find_element(By.CSS_SELECTOR, "[class='checkout__text']").click()
    def cautare_fotografie(self):
        self.driver.get("https://carturesti.ro/")
        self.driver.find_element(By.XPATH, "//input[@id='search-input']").send_keys("fotografie")
        self.driver.find_element(By.CSS_SELECTOR, "[placeholder='Căutare']").send_keys(Keys.ENTER)
    def pret_ascendent(self):
        self.sort_by_price_element = driver.find_element(By.CSS_SELECTOR, "[id='select_option_46']")
        self.sort_by_price_element.value_of_css_property("Preț (ascendent)")
    def revista_matca(self):
        self.driver.get("https://carturesti.ro/")
        self.driver.find_element(By.XPATH, "//input[@id='search-input']").send_keys("Revista Matca Nr. 1")
        self.driver.find_element(By.CSS_SELECTOR, "[placeholder='Căutare']").send_keys(Keys.ENTER)
        self.driver.find_element(By.CSS_SELECTOR, "[title='Revista Matca. Nr. 1']")
        self.driver.find_element(By.CSS_SELECTOR, "[title='Adaugă în coș']")
    def add_checkout(self):
        self.driver.get("https://carturesti.ro/checkout")
        self.driver.find_element(By.XPATH, "//input[@id='product-2148909063-quantity']").send_keys("3")
    def librarii(self):
        self.driver.get("https://carturesti.ro/librarii")
        self.driver.find_element(By.CSS_SELECTOR, "[data-coordinates-lng='23.628259']")
    def retur(self):
        self.driver.get("https://carturesti.ro/")
        self.driver.find_element(By.CSS_SELECTOR, "[href='/info/politica-confidentialitate']").click()
    def newsletter(self):
        self.driver.get("https://carturesti.ro/")
        self.driver.find_element(By.XPATH, "//input[@id='mce-EMAIL']").send_keys("nume.prenume@yahoo.com")
        self.driver.find_element(By.CSS_SELECTOR, "[id='mce-FNAME']").send_keys("Popescu")
        self.driver.find_element(By.CSS_SELECTOR, "[id='mce-LNAME']").send_keys("Maria")
        self.driver.find_element(By.CSS_SELECTOR, "[id='mc-embedded-subscribe']").click()
    def voucher_cadou(self):
        self.driver.get("https://carturesti.ro/")
        self.driver.find_element(By.CSS_SELECTOR, "[class='md-raised md-button md-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[id='ordercoupon-text']").send_keys("La mulți ani!")
        self.driver.find_element(By.CSS_SELECTOR, "[id='ordercoupon-quantity']").send_keys("2")
        self.driver.find_element(By.CSS_SELECTOR, "[id='ordercoupon-price_gross']").send_keys("200")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()


