Feature: Create a user in go rest database
  Scenario: Create a User using valid data
    Given A user with valid access token
      And the user has email as "subornosamonto@gmail.com"
      And the user wants to create a record with name as "Subarna"
      And the gender is "male"
      And the user status is "active"
    When user submits the user data in "https://gorest.co.in/public-api/users"
      Then you should receive a "200" status code
      And mail is "subornosamonto@gmail.com"
      And first name "Subarna" should be in response body
      And gender "male" should be in response body
      And user status "active" should be in response body
