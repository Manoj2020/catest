@getpepsbyid
Feature: Get PEPS by Id
        This feature is part of the API that services politician data.
  Scenario Outline: Create politicians with valid data
      Given I have access to the politician API Service Environment
      And I build the endpoint to access politician API
      And I build the HTTP header details
      When I send the GET peps by "<id>" request
  	  Then I verify the response http code is 200
      Then I validate GET by ID response json schema
      And I validate the returned "<name>" in the response
      And I check the "<country>" in the response
      And I validate the "<position>" returned in the response
      And I validate the "<risk>" in the returned response
      And I examine the returned "<yob>" in the response

      Examples:
      | id 			              | name 		| country 			| yob   | position    			    | risk	|
      | 5efc7a090f0698013cf20a96  | John Doe  	| Wales  			| 1970 	| Minister of Perry	        | 1 	|
      | 5efc5ba40f069801301a458c  | John Smith  | England  			| 1980 	| Minister of Ales		    | 2 	|
      | 5efc5ab60f069801301a4589  | Jane Doe  	| Scotland  		| 1981 	| Minister of Single Malts  | 3 	|
      | 5efc5ab60f069801301a458a  | Jane Smith  | Nothern Ireland  	| 1982 	| Minister of Guinness  	| 4     |

