@getpeps
Feature: Get PEPS
        This feature is part of the API that services politician data.
  Scenario: Get politicians
      Given I have access to the politician API Service Environment
      And I build the endpoint to access politician API
      And I build the HTTP header details
      When I send the GET request
  	  Then I verify the response http code is 200
      Then I validate GET response json schema
      Then I validate that they are in descending order by date of creation
      Then I validate the response has 5 politicians records

