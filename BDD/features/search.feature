Feature:
  Scenario Outline: Cauta lista de produse dupa "fotografie"
    Given I am on the home page
    When I search for the fotografie
    Then I see a list of products about fotografie
    Examples:
      |fotografie  |

  Scenario: Cauta produsul "fotografie" dupa pretul ascentent
    Given I am on https://carturesti.ro/product/search/fotografie
    When I select the filters
    When I click on pret ascendent
    Then I see the all products with pret ascendent

  Scenario: Cauta produsul "fotografie" dupa disponibilitate
    Given I am on https://carturesti.ro/product/search/fotografie
    When I select the filters
    When I click on Livrare 24h
    Then  I see the all products with Livrare 24h


