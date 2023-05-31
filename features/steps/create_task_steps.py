from behave import *
from selenium import webdriver
from configuration.config import TestData
from pages.LoginPage import LoginPage
from pages.my_app_page import MyAppPage
from pages.my_task_page import MyTaskPage
from pages.sub_task_page import SubTaskPage


@given(u'Launch the browser')
def launch_browser(context):
    if TestData.BROWSER == 'chrome':
        context.driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH)
    elif TestData.BROWSER == 'firefox':
        context.driver = webdriver.Firefox(executable_path=TestData.FIREFOX_EXECUTABLE_PATH)
    else:
        raise ValueError('Browser is not supported')


@when(u'Open the https://qa-test.avenuecode.io/users/sign_in website')
def open_login_page(context):
    try:
        context.driver.get(TestData.URL)
        context.loginPage = LoginPage(context.driver)
        context.myapppage = MyAppPage(context.driver)
        context.mytaskpage = MyTaskPage(context.driver)
        context.subtaskpage = SubTaskPage(context.driver)
    except:
        context.driver.close()
        assert False,"Test is failed in open login page section"


@then(u'The login portal has been opened')
def validate_login_page(context):
    try:
        context.loginPage.validate_title()
    except:
        context.driver.close()
        assert False, "Test is failed in validate login page title"


@then(u'Provide the username "{user}" and password "{pwd}"')
def enter_login_creds(context, user, pwd):
    try:
        context.loginPage.enter_login_credentials(user,pwd)
    except:
        context.driver.close()
        assert False, "Test is failed in enter login credentials"


@then(u'Click on the Login button')
def enter_login(context):
    try:
        context.loginPage.enter_login()
    except:
        context.driver.close()
        assert False, "Test is failed in enter login"


@then(u'Login is successful and dashboard is opened')
def validate_dashboard_page(context):
    try:
        context.myapppage.validatePageLoaded()
    except:
        context.driver.close()
        assert False, "Test is failed in validating dashboard"


@then(u'Provide the password "{pwd}"')
def enter_login_creds(context, pwd):
    try:
        context.loginPage.enter_password(pwd)
    except:
        context.driver.close()
        assert False, "Test is failed in enter password"


@then(u'Provide the username "{user}"')
def enter_login_creds(context, user):
    try:
        context.loginPage.enter_username(user)
    except:
        context.driver.close()
        assert False, "Test is failed in enter username"


@then(u'Click on the My Tasks button')
def enter_on_my_task(context):
    try:
        context.loginPage.enter_on_my_task()
    except:
        context.driver.close()
        assert False, "Test is failed when tried to enter on My Task."


@then(u'Click and write in the text_box the new Task "{task}"')
def create_new_task(context, task):
    try:
        context.mytaskpage.validate_page()
        context.mytaskpage.create_new_task_and_send_enter(task)
    except:
        context.driver.close()
        assert False, "Test is failed when tried to enter on My Task."


# @then(u'CIt is possible to create subtasks clicking on the add task button.')
# def create_new_task(context, task):
#     try:
#         context.mytaskpage.validate_page()
#         context.mytaskpage.create_new_task_and_send_enter(task)
#     except:
#         context.driver.close()
#         assert False, "Test is failed when tried to enter on My Task."


@then(u'We can not see this welcome message: "{message}"')
def create_new_task(context, message):
    try:
        context.mytaskpage.validate_page(message)
    except:
        context.driver.close()
        assert False, "Test is failed when tried to enter on My Task."


@then(u'Click and write in the text_box the new Task "{task}" and check If appear on the top of list')
def create_new_task(context, task):
    try:
        context.mytaskpage.validate_page()
        context.mytaskpage.create_new_task_and_send_enter(task)
    except:
        context.driver.close()
        assert False, "Test is failed when tried to enter on My Task."


@then(u'Create a task If dooes not exist and after that click on Manage Subtasks.')
def enter_on_subtask(context):
    try:
        context.loginPage.enter_on_my_task()
        context.mytaskpage.validate_page()
        context.mytaskpage.check_if_exist_task_and_add_sub_Task()
        context.subtaskpage.validate_page()
    except:
        context.driver.close()
        assert False, "Test is failed when tried to enter on My Task."


@then(u'Create a sub task after that check the number of sub task "{subtask}" "{duedate}"')
def check_number_of_sub_tasks(context, subtask, duedate):
    try:
        context.loginPage.enter_on_my_task()
        context.mytaskpage.validate_page()
        context.mytaskpage.check_if_exist_task_and_add_sub_Task()
        context.subtaskpage.validate_page()
        context.subtaskpage.create_sub_task(subtask, duedate)
        number_of_subtasks = context.mytaskpage.check_number_of_sub_tasks()
        print(f"numeros: {number_of_subtasks}")
        context.subtaskpage.check_number_of_sub_tasks(number_of_subtasks)

    except:
        context.driver.close()
        assert False, "Test is failed when tried to enter on My Task."


@then(u'Edit the task and check the new title "{new_title}"')
def edit_a_task_using_sub_Task_pop_ups(context, new_title):
    try:
        context.loginPage.enter_on_my_task()
        context.mytaskpage.validate_page()
        context.mytaskpage.enter_on_subtask()
        context.subtaskpage.validate_page()
        text = context.subtaskpage.edit_task(new_title)
        context.mytaskpage.check_new_title_of_task(text)
    except:
        context.driver.close()
        assert False, "Test is failed when tried to enter on My Task."


@then(u'Click and write in the text_box the new SubTask "{subtask}" "{duedate}"')
def create_new_subtask_with_more_than_250_characters(context, subtask="", duedate=""):
    try:
        context.loginPage.enter_on_my_task()
        context.mytaskpage.validate_page()
        context.mytaskpage.enter_on_subtask()
        context.subtaskpage.validate_page()
        context.subtaskpage.create_sub_task(subtask, duedate)

    except:
        context.driver.close()
        assert False, "Test is failed when tried to write a new subtask with more than 250 characters."


@then(u'Click and write in the text_box the new SubTask empty.')
def create_new_subtask_with_more_than_250_characters(context, subtask="", duedate=""):
    try:
        context.loginPage.enter_on_my_task()
        context.mytaskpage.validate_page()
        context.mytaskpage.enter_on_subtask()
        context.subtaskpage.validate_page()
        context.subtaskpage.create_sub_task(subtask, duedate)

    except:
        context.driver.close()
        assert False, "Test is failed when tried to write a new subtask with more than 250 characters."


@then(u'Close the browser')
def step_impl(context):
    context.driver.close()