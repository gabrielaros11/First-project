Feature: newsletter functionality
  @newsletter
  Scenario: subscribe to the newsletter
    Given I am on the home page and I am looking for the Abonează-te la newsletter
    When I input my email
    And I input my last name
    And I input my first name
    And I click on ABONARE button
    Then I should subscribe to the newsletter