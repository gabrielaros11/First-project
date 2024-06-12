Feature: login functionality
  @login
  Scenario: connected successfully
    Given I am on the home page
    Given I am on Login page
    When I click on the Utilizator Existent
    And I input my email
    And I input my password
    And I click on Autentificare button
    Then I should be signed in to my account

  Scenario: login failed
    Given I am on Login page
    When I click on the Utilizator Existent
    And I input my email
    And I input a wrong password
    And I click on AUTENTIFICARE button
    Then I get the following error message "Adresă de email sau parolă incorectă."



