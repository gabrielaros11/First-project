import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.bidi import console
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# 1. Selecteaza browserul
driver = webdriver.Chrome()
# 2. Maximizeaza browserul
driver.maximize_window()
# 3. Acceseaza site-ul
driver.get("https://carturesti.ro/")
# 4. Accepta cookies
driver.find_element(By.CSS_SELECTOR, "[aria-label='allow cookies']").click()
# 5. Cauta domeniul de interes
driver.find_element(By.XPATH, "//input[@id='search-input']").send_keys("fotografie")
driver.find_element(By.CSS_SELECTOR, "[placeholder='Căutare']").send_keys(Keys.ENTER)
time.sleep(2)
# 6. Sorteaza dupa "Livrare 24h"
driver.find_element(By.CSS_SELECTOR, "[data-ng-bind='::option.label']").click()
time.sleep(4)
# 7. Sorteaza dupa "Pret ascendent"
sort_by_price_element = driver.find_element(By.CSS_SELECTOR, "[id='select_option_46']")
sort_by_price_element.value_of_css_property("Preț (ascendent)")
time.sleep(3)
# 8. Verifica daca sortarea dupa "Pret ascendent" a fost executata
price_values = sort_by_price_element
if price_values == price_values:
  print("Sortarea după preț (ascendent) a fost aplicată cu succes!")
else:
  print("Sortarea după preț (ascendent) nu a fost aplicată cu succes!")
driver.get("https://carturesti.ro/product/search/fotografie?stock_label=livrare-24&sort-by=price%20asc")

# 9. Selecteaza o carte
def select_a_book(driver, book_title):
  book_title.click()
  print("Carti postale Icons of Style - Mai multe modele")

#10. Verifica daca pagina cartii a fost deschisa
book_title = "Carti postale Icons of Style - Mai multe modele"
if book_title == book_title:
    print(f"Cartea '{book_title}' a fost selectată cu succes!")
else:
    print(f"A apărut o eroare la selectarea cărții '{book_title}'.")

#11. Liste
#adaugare lista_carte
lista_carte = ["Arta, arhitectura", "Filosofie", "Psihologie"]
print(lista_carte)

#adaugare lista_reviste
lista_reviste = ["Reviste - Limba romana", "Reviste - Limbi straine"]
print(lista_reviste)

#stergere "Reviste - Limba romana" din lista_reviste
lista_reviste.remove("Reviste - Limba romana")
print(lista_reviste)

#stergere elementul 0 din lista_carte, adica "Arta, arhitectura"
lista_carte.pop(0)
print(lista_carte)

#12. Set-uri
#adaugare set
set = ["Muzica", "Film"]
print(set)

#stergere elementul "Film"
set.remove("Film")
print(set)

#adaugare un element pe indexul 1 cu numele "Jocuri si jucarii"
set.insert(1, "Jocuri si jucarii")
print(set)

#13. Tuple-uri
#adaugarea tuple
tuple = ["Rafturi alese", "Scolaresti", "Papetarie"]
print(tuple)

#printare elementul 2 din tuple
print(tuple[2])

#14. Dictionare
primul_dictionar = {"carte" : "Fata din fotografie",
                    "autor" : "JORDYN TAYLOR",
                    "limba" : "romana",
                    "numar pagini" : "336"}

# print(f"Cartea {carte} este scrisa de {autor} in limba {limba} si are {numar pagini} pagini")
# printeaza toate elementele primului dictionar
print(primul_dictionar["carte"])
print(primul_dictionar["autor"])
print(primul_dictionar["limba"])
print(primul_dictionar["numar pagini"])

# printeaza numele filmului
al_doilea_dictionar = {"categoria" : "Film",
                       "detalii film" : {"nume" : "Cinema Paradiso (4K Ultra HD)",
                                         "Regizor" : "Giuseppe Tornatore",
                                         "Tara de origine": "Italia",
                                         "Data publicarii" : "1988"}}
print(al_doilea_dictionar["detalii film"]["nume"])

# schimba categoria dictionarului
al_doilea_dictionar.update({"categoria" : "Carte"})
print(al_doilea_dictionar)

# se elimina elementul "detalii film" din al_doilea_dictionar
al_doilea_dictionar.pop("detalii film")
print(al_doilea_dictionar)

#15.Check out - verificam cate produse sunt in cosul de cumparaturi
driver.get("https://carturesti.ro/checkout")
time.sleep(5)
produse_in_cos = 0
def checkout():
    if produse_in_cos != 0:
        return "Exista produse in cosul de cumparaturi"
    elif produse_in_cos >= 0:
        return "Nu mă lăsa gol"
print(checkout())

