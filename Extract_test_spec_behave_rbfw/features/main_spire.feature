Feature: Extract data from word document
  Scenario: Get test case from word doc
#    Given Test spec word doc "C:\Github\PycharmProjects\Extract_test_spec_behave_rbfw\DEV-0044600 STMN IOS Main Application Verification Specifications Rev 4.docx"
    Given Test spec word doc
    When process the data extracted
    Then the output is dictionary structure