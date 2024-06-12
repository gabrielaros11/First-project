Feature: gift card
  @voucher
  Scenario: add to cart 2 gift cards
    Given I am on the home page
    When I see Vrei să iei un voucher cadou pentru cineva drag ție?
    And I click on COMANDA-L AICI button
    Then I see the cupon checkout page
    And I input La mulți ani!
    And I input 2 on Cantitate tab
    Then I input 200 on Valoare tab
    And I click on COMANDA
    Then I am on sign up page