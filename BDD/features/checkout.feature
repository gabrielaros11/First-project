Feature: checkout functionality
  @checkout
    Scenario: empty cart
      Given I am on checkout page
      When I click on Cosul tau
      Then I see Cosul tau este gol

    Scenario: add more product in the cart
      Given I am on checkout page
      When I see one product in the cart
      And I add 2 more
      Then I see 3 products in the cart