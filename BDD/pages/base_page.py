from BDD import Browser


class BasePage(Browser):
    def navigate_carturesti(self):
        self.driver.get("https://carturesti.ro/")
