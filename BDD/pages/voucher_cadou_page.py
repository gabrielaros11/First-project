from selenium.webdriver.common.by import By

from pages.base_page import Base_Page


class Voucher_cadou(Base_Page):
    def voucher_cadou(self):
        self.driver.get("https://carturesti.ro/")
        self.driver.find_element(By.CSS_SELECTOR, "[class='md-raised md-button md-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[id='ordercoupon-text']").send_keys("La mulți ani!")
        self.driver.find_element(By.CSS_SELECTOR, "[id='ordercoupon-quantity']").send_keys("2")
        self.driver.find_element(By.CSS_SELECTOR, "[id='ordercoupon-price_gross']").send_keys("200")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()