@createpeps
Feature: Create PEPS
        This feature is part of the API that services politician data

  Scenario Outline: Create politicians with valid data
      Given I have access to the politician API Service Environment
      And I build the endpoint to access politician API
      And I build the HTTP header details
      And I build create peps POST http body with "<name>", "<country>", "<yob>", "<position>" and "<risk>" details
      When I send the POST request
  	  Then I verify the response http code 201
      Then I validate POST response json schema
      And I validate response message generated id is not null
      And I validate response message ok is true
      And I validate message field value
      And I validate response id value is not null

      Examples: validData
      | name 			| country 			| yob   | position    			    | risk	|
      | John Doe  	    | Wales  			| 1970 	| Minister of Perry	        | 1 	|
      | John Smith  	| England  			| 1980 	| Minister of Ales		    | 2 	|
      | Jane Doe  	    | Scotland  		| 1981 	| Minister of Single Malts  | 3 	|
      | Jane Smith  	| Nothern Ireland  	| 1982 	| Minister of Guinness  	| 4     |



  Scenario Outline: Create politicians with invalid data
      Given I have access to the politician API Service Environment
      And I build the endpoint to access politician API
      And I build the HTTP header details
      And I build create peps POST http body with "<name>", "<country>", "<yob>", "<position>" and "<risk>" details
      When I send the POST request
  	  Then I verify the response http code is not 201
      And I validate response message ok is not true
      And I validate message field value is not successful
      And I validate response id value is null

      Examples: invalidData
      | name 			    | country 			| yob    		| position    			    | risk	| testcase_descrption   |
      | John Doe  	        | Wales  			| 1970 	        | Minister 	of Perry	    | 10 	| risk is above 5       |
      | John Smith  	    | England  			| 2025 	        | Minister of Ales		    | 2 	| dob is a future date  |
      | Jane Doe  	        | Scotland  		| 1600 	        | Minister of Single Malts  | 3 	| dob is a very old     |
      | Jane Smith  	    | Nothern Ireland  	| 1982 	        | Minister of Guinness  	| 4     | duplicate record      |
      | !"£n#~@@@@@"£$      | Wales  			| 1970 	        | Minister 	of Perry	    | 1 	| invalid name          |
      | John Smith  	    | Pen island		| 202025        | Minister of Ales		    | 2 	| invalid year format   |
      | Jane Doe  	        | Scotland  		| 2006 	        | Minister of Single Malts  | 3 	| person is a minor     |
      | Inglorious Bastard  | United Kingdom    | 1982 	        | Prime Minister  	        | 5     | wrong information     |


