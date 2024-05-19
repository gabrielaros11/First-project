# Scenarii simple

Feature: Login
  Scenario: Connected successfully
    Given I am on Login page
    When I click on the Utilizator Existent
    And I input my email
    And I input my password
    And I click on Autentificare button
    Then I should be signed in to my account

  Scenario: Login failed with wrong password
    Given I am on Login page
    When I click on the Utilizator Existent
    And I input my email
    And I input a wrong password
    And I click on AUTENTIFICARE button
    Then I should get an error message

# Scenariu parametrizat
  Scenario Template: Filter products by pret ascendent
    Given I select the filters
    When I click on pret ascendent
    Then I see the all products with pret ascendent
    Examples:
      | pret ascendent |

# Scenariu outline
  Scenario Outline: Browse the website
    Given I am on the home page www.carturesti.ro
    When I search for the carte
    Then I see a list of carte
    Examples:
      | carte |

