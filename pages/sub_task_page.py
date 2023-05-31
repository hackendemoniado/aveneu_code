import time

from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class SubTaskPage(BasePage):
    TXT_VALIDATE_PAGE = (By.XPATH, "//h3[contains(text(),'Editing Task')]")
    INPUT_SUBTASK = (By.ID,"new_sub_task")
    INPUT_DUEDATE_SUBTASK = (By.ID,"dueDate")
    BTN_ADD_SUB_TASK = (By.ID,"add-subtask")
    BTN_CLOSE_SUB_TASK = (By.XPATH,"//button[contains(text(),'Close')]")
    FIRST_SUB_TASK = (By.XPATH, "(//td[@class='task_body col-md-8 limit-word-size'])[1]")
    LIST_OF_SUB_TASKS = (By.XPATH, "//td[@class='task_body col-md-8 limit-word-size']")
    INPUT_TASK = (By.ID, "edit_task")

    def __init__(self, driver):
        super().__init__(driver)

    def validate_page(self, message=''):
        if "Editing Task" in self.get_element_text(self.TXT_VALIDATE_PAGE):
            assert True

    def create_sub_task(self, subtask, duedate):
        if subtask != "" or duedate != "":
            self.input_element(self.INPUT_SUBTASK, subtask)
            self.input_element(self.INPUT_DUEDATE_SUBTASK, duedate)
            self.click_element(self.BTN_ADD_SUB_TASK)
            assert self.get_element_text(self.FIRST_SUB_TASK) == subtask
        else:
            self.input_element(self.INPUT_SUBTASK, subtask)
            print("tratando de limpiar duedate")
            self.clear_input_element(self.INPUT_DUEDATE_SUBTASK)
            self.click_element(self.BTN_ADD_SUB_TASK)
            assert self.get_element_text(self.FIRST_SUB_TASK) == "empty"
        self.click_element(self.BTN_CLOSE_SUB_TASK)

    def check_number_of_sub_tasks(self, number_of_subtasks):
        print(f"entrando al ultimo check: {number_of_subtasks}")
        assert len(self.get_elements(self.LIST_OF_SUB_TASKS)) == number_of_subtasks

    def edit_task(self, task="Edited using subtask"):
        print("edit_task")
        self.input_element(self.INPUT_TASK, task)
        print(f"nuevo titulo: {self.get_element_text(self.INPUT_TASK)}")
        title = self.get_element_text(self.INPUT_TASK)
        self.click_element(self.BTN_CLOSE_SUB_TASK)
        return title
