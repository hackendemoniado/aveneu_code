import re

from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class MyTaskPage(BasePage):
    TXT_VALIDATE_PAGE = (By.XPATH, "//h1[contains(text(),'Sergio')]")
    TXT_NEW_TASK = (By.ID, "new_task")
    CHECK_TASK = (By.XPATH, "(//a[@class='ng-scope ng-binding editable editable-click'])[1]")
    LIST_TASK = (By.XPATH, "//a[@class='ng-scope ng-binding editable editable-click']")
    ADD_BUTTON = (By.XPATH, "//span[@class='input-group-addon glyphicon glyphicon-plus']")
    ADD_SUBTASK = (By.XPATH, "(//button[@class='btn btn-xs btn-primary ng-binding'])[1]")

    def __init__(self, driver):
        super().__init__(driver)

    def validate_page(self, message=''):
        if message == '':
            assert self.get_element_text(self.TXT_VALIDATE_PAGE) == "Sergio Gonzalez's ToDo List"
        else:
            assert self.get_element_text(self.TXT_VALIDATE_PAGE) != message

    def create_new_task_and_send_enter(self, task):
        self.input_element(self.TXT_NEW_TASK, task)
        self.send_enter(self.TXT_NEW_TASK)
        assert self.get_element_text(self.CHECK_TASK) == task

    def create_new_task_and_check_top_of_list(self, task):
        self.input_element(self.TXT_NEW_TASK, task)
        self.send_enter(self.TXT_NEW_TASK)
        list = self.get_elements(self.LIST_TASK)
        assert self.get_element_text(list[0]) == task

    def check_if_exist_task_and_add_sub_task(self, task="task to add sub task"):
        list_of_tasks = self.get_elements(self.LIST_TASK)
        if len(list_of_tasks) == 0:
            self.input_element(self.TXT_NEW_TASK, task)
            self.send_enter(self.TXT_NEW_TASK)
            assert self.get_element_text(self.CHECK_TASK) == task
        self.click_element(self.ADD_SUBTASK)

    def enter_on_subtask(self):
        self.click_element(self.ADD_SUBTASK)

    def check_number_of_sub_tasks(self):
        subtask = self.get_element_text(self.ADD_SUBTASK)
        nums = [int(match.group(1)) for match in re.finditer(r"\((\d+)\)", subtask)]
        self.click_element(self.ADD_SUBTASK)
        return nums[0]

    def create_new_task_and_press_on_add_button(self, task):
        self.input_element(self.TXT_NEW_TASK, task)
        self.click_element(self.ADD_BUTTON)
        assert self.get_element_text(self.CHECK_TASK) == task

    def check_new_title_of_task(self, text):
        assert self.get_element_text(self.TXT_NEW_TASK) == text
