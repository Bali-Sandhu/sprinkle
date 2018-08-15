Feature: Login
  In order to use the app
  As a user
  I must Login with the correct credentials

Background:
  Given the Login form is displayed

  Scenario: Login with valid Login credentials
    When I enter valid credentials
    And I submit the Login Form
    Then a welcome message is displayed

  Scenario Outline: Login with invalid Login credentials
    When the user enters <username>
    And the user enters <password>
    And clicks Login
    Then the user is presented with a error message

  Examples:
  |username|password|
  |test@tes.com|password1234|

     Scenario: Attempt Login without credentials
     When I submit the Login form without credential
     Then the user is presented with an error message

#   Scenario: Login with incorrect username
#     Given the user has the incorrect credentials
#     When the user enters username
#     And the user enters password
#     And clicks Login
#     Then the user is presented with a error message
#
#
#  Scenario: Login with incorrect password
#    Given the user has the incorrect credentials
#    When the user enters username
#    And the user enters password
#    And clicks Login
#    Then the user is presented with a error message