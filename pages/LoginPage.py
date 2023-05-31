from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    TXT_USERNAME = (By.ID, "user_email")
    TXT_PASSWORD = (By.ID, "user_password")
    BTN_LOGIN = (By.XPATH, "//input[@class='btn btn-primary']")
    INVALID_CREDENTIALS = (By.XPATH, "//div[@class='alert alert-warning']")
    BTN_MYTASK = (By.ID, "my_task")

    def __init__(self, driver):
        super().__init__(driver)

    def enter_login_credentials(self, user, pwd):
        self.input_element(self.TXT_USERNAME, user)
        self.input_element(self.TXT_PASSWORD, pwd)

    def enter_username(self,user):
        self.input_element(self.TXT_USERNAME, user)

    def enter_password(self, pwd):
        self.input_element(self.TXT_PASSWORD, pwd)

    def enter_login(self):
        self.click_element(self.BTN_LOGIN)

    def validate_title(self):
        assert self.get_title() == "QA Assessment"

    def enter_on_my_task(self):
        self.click_element(self.BTN_MYTASK)
