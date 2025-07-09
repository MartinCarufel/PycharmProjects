Feature: Extract test case data from word file

  @First_tag
  Scenario: Test the extracted data format
    Given Test spec in word file format
    When process the word file
    Then the extracted data is a dictionary


  Scenario: Test collect all test cases
    Given Test spec in word file format
    When process the word file
    Then the number of test case match

  Scenario: Test collect proper number of step
    Given Test spec in word file format
    When process the word file
    Then the number of test step match

  @second_tag
  Scenario: Requirement formating
    Given Test case in word
    When processing requirement formating
    Then the result is formated as CSV



  # Install allure
  # First install scoop
  # In power shell set policy
  # Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
  # iwr -useb get.scoop.sh | iex
  # Confirm with scoop help
  # Install allure
  # scoop install allure
  # Install behave allure
  # pip install allure-behave

  # run with allure report
  # behave -f allure_behave.formatter:AllureFormatter o my_allure

  # behave --no-capture -f json.pretty .\features\main_spire_test.feature .\features\main_spire_test.feature

  # run with report json
  # behave --no-capture -f json.pretty -o .\reports\report.json .\features\main_spire_test.feature# run with report

  # Run with report junit
  # behave --no-capture --junit -o .\reports\report.txt .\features\main_spire_test.feature