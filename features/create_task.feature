Feature: As a ToDo App user
I should be able to create a task
So I can manage my tasks

  Background:
    Given Launch the browser
    When Open the https://qa-test.avenuecode.io/users/sign_in website
    Then The login portal has been opened

  Scenario: It is possible to create subtasks by pressing "Enter".
    And Provide the username "sergiosysforence@hotmail.com.ar" and password "Qualityassurance"
    And Click on the Login button
    Then Login is successful and dashboard is opened
    Then Click on the My Tasks button
    Then Click and write in the text_box the new Task "new task using Enter"

  Scenario: It is possible to create subtasks clicking on the add task button.
    And Provide the username "sergiosysforence@hotmail.com.ar" and password "Qualityassurance"
    And Click on the Login button
    Then Login is successful and dashboard is opened
    Then Click on the My Tasks button
    Then Click and write in the text_box the new Task "new task using button +"

  Scenario: The required welcome message does not appear.
    And Provide the username "sergiosysforence@hotmail.com.ar" and password "Qualityassurance"
    And Click on the Login button
    Then Login is successful and dashboard is opened
    Then Click on the My Tasks button
    Then We can not see this welcome message: "Hey Sergio, this is your todo list for today:"

  Scenario: The required welcome message does not appear.
    And Provide the username "sergiosysforence@hotmail.com.ar" and password "Qualityassurance"
    And Click on the Login button
    Then Login is successful and dashboard is opened
    Then Click on the My Tasks button
    Then We can not see this welcome message: "Hey Sergio, this is your todo list for today:"

  Scenario: The minimum of 3 characters is not respected when the task is created.
    And Provide the username "sergiosysforence@hotmail.com.ar" and password "Qualityassurance"
    And Click on the Login button
    Then Login is successful and dashboard is opened
    Then Click on the My Tasks button
    Then Click and write in the text_box the new Task "1"

  Scenario: The maximum of 250 characters is not respected when the task is created.
    And Provide the username "sergiosysforence@hotmail.com.ar" and password "Qualityassurance"
    And Click on the Login button
    Then Login is successful and dashboard is opened
    Then Click on the My Tasks button
    Then Click and write in the text_box the new Task "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium q"

  Scenario: When added, the task should be appended on TOP of the list of created tasks.
    And Provide the username "sergiosysforence@hotmail.com.ar" and password "Qualityassurance"
    And Click on the Login button
    Then Login is successful and dashboard is opened
    Then Click on the My Tasks button
    Then Click and write in the text_box the new Task "2" and check If appear on the top of list

  Scenario: Create a task If dooes not exist and after that click on Manage Subtasks.
    And Provide the username "sergiosysforence@hotmail.com.ar" and password "Qualityassurance"
    And Click on the Login button
    Then Login is successful and dashboard is opened
    Then Click on the My Tasks button
    Then Create a task If dooes not exist and after that click on Manage Subtasks.

  Scenario: This button should have the number of subtasks created for those tasks
    And Provide the username "sergiosysforence@hotmail.com.ar" and password "Qualityassurance"
    And Click on the Login button
    Then Login is successful and dashboard is opened
    Then Click on the My Tasks button
    Then Create a task If dooes not exist and after that click on Manage Subtasks.
    Then Create a sub task after that check the number of sub task "Subtask" "05/30/2023"

  Scenario: The task description field is not read-only when trying to create a subtask.
    And Provide the username "sergiosysforence@hotmail.com.ar" and password "Qualityassurance"
    And Click on the Login button
    Then Login is successful and dashboard is opened
    Then Click on the My Tasks button
    Then Edit the task and check the new title "Edited using subtask"

Scenario: The maximum of 250 characters is not respected when the subtask is created.
    And Provide the username "sergiosysforence@hotmail.com.ar" and password "Qualityassurance"
    And Click on the Login button
    Then Login is successful and dashboard is opened
    Then Click on the My Tasks button
    Then Click and write in the text_box the new SubTask "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium q" "30/05/2023"

Scenario: The date when creating a subtask does not validate its format.
    And Provide the username "sergiosysforence@hotmail.com.ar" and password "Qualityassurance"
    And Click on the Login button
    Then Login is successful and dashboard is opened
    Then Click on the My Tasks button
    Then Click and write in the text_box the new SubTask "new subtask" "05/31/2023"

Scenario: When creating a subtask it is possible to enter any text in the date.
    And Provide the username "sergiosysforence@hotmail.com.ar" and password "Qualityassurance"
    And Click on the Login button
    Then Login is successful and dashboard is opened
    Then Click on the My Tasks button
    Then Click and write in the text_box the new SubTask "new subtask" "asdasdasd"

  Scenario: When We create a new subtask, date and description could by empty.
    And Provide the username "sergiosysforence@hotmail.com.ar" and password "Qualityassurance"
    And Click on the Login button
    Then Login is successful and dashboard is opened
    Then Click on the My Tasks button
    Then Click and write in the text_box the new SubTask empty.
