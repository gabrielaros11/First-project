Feature: bookstore functionality
  @bookstore
  Scenario: search map of the bookstore
#    Given I am on Librării page
#    When I click on HARTA - Carturesti Iulius Mall Cluj
#    Then I see the map of Carturesti Iulius Mall Cluj

  Scenario: search instagram page of the bookstore
    Given I am on Librării page
    When I click on carturesti_verona
    Then I see the instagram page of Carturesti Verona
