from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MyAppPage(BasePage):
    TXT_MYAPP = (By.XPATH, "//h1[contains(text(),'QA Assessment')]")

    def __init__(self, driver):
        super().__init__(driver)

    def validatePageLoaded(self):
        self.verify_element_displayed(self.TXT_MYAPP)
        assert self.get_element_text(self.TXT_MYAPP) == "QA Assessment"
