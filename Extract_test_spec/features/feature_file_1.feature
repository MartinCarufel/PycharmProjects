Feature: Word test spec data extraction
  I want to extract all test case title and step definition from word document


  Scenario: Data extracted in dictionary
    Given Test spec word document
    When The fetch doc method is called
    Then the fetch doc method return a structured dictionary
    And the dictionary is not empty

