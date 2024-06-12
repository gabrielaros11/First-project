Feature: checkout functionality
  @basket
  Scenario: add product to cart
    Given I am on the home page
#    When I click on search bar
    When I input "Revista Matca nr. 1"
    And I click on "Revista Matca. Nr. 1"
    And I click on Adauga in cos
#    Then I see one product in the cart with Revista Matca Nr. 1
