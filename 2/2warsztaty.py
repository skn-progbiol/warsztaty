"""
Przypomnienie+:
1. typy danych
2. sprawdzanie typu przy użyciu type()
3. instrukcje warunkowe - ify
4. print()
5. zamiana jednego typu danych na drugi:
int(), float(), str() i bool()
6. zadanie:
Napisz program, który przyjmie nazwę waluty, na ktorą chcemy zamienić
złotowki i przyjmie kwotę, ktorą na tę walutę przeliczy
1 euro = 4.2671 zl
1 dolar = 3.8399 zl
1 GBP = 4.9378 zl
Za pomocą # można komentować, tzn. zapisać linijkę, którą python
zignoruje. W przypadku potrójnych cudzysłowów, jak to zrobiłam tutaj,
ignoruje całą zawartość pomiędzy nimi. Można to wykorzystywać np., żeby
sprawdzać działanie tylko określonych linijek kodu.
"""

#6 - program:
print('Wybierz kwote oraz walute')
waluta = input("waluta: ")
kwota = input('kwota: ')
if waluta == "euro":
    print(float(kwota)/ 4.2671)
if waluta == "dolar" :
    print(float(kwota)/ 3.8399)
if waluta == "funt" :
    print(float(kwota)/ 4.9378)

"""
LISTY
Struktura, które może zawierać wiele różnych wartości, zapisywane w [ ], np.
[11, 4, "item", 7.98, True, 9, "item2"]
Każdy element listy ma przypisany index, tzn. pozycję w tej liście.
>>>są one liczone od 0<<<
["a", "b", "c", "d", "e"]
  0    1    2    3    4
Elementy można wywoływać, podając ich indexy:
"""

animals = ['cat', 'rat', 'deer', 'elephant', 'bat', "dog", "mouse"]

print(animals[0]) #wyswietli 'cat'
print(animals[5]) #wyswietli 'dog'
"""
Można też wywoływać kilka elementów, stosując slicing. Podajemy przedział
[początek:koniec], przy czym uwaga:
>>>przedział jest prawostronnie otwarty, tzn. nie wyświetli się element
z indexem równym koniec<<<:
"""
print(animals[0:3]) #wyswietli ['cat', 'rat', 'deer']
print(animals[1:4])

"""
Kiedy nie poda się początku i/lub końca, to wyświetli się wszystko z danej
"strony":
"""
print(animals[:4])
print(animals[2:])
print(animals[:])

"""
Elementy można numerować też od tyłu, tj.
["a", "b", "c", "d", "e"]
  -5  -4    -3   -2   -1
"""
print(animals[-3])
print(animals[-3:-1])

"""
W slicingu można też określić, co ile elementów się przeskakuje
[początek:koniec:skok]
"""
print(animals[::1]) #wszystkie elementy, bo co jeden
print(animals[::2]) #co drugi element

print(animals[::-1]) #lista od tyłu

"""Listy można też zagnieżdżać (nesting), tzn. umieszczać listy w listach"""

gniazdo = ["kura", "gęś", "kaczka", ["wróbel", "gołąb", "dzięcioł"]]

print(gniazdo[3]) #wyświetlenie 3 elementu, czyli zagnieżdżonej listy
print(gniazdo[3][1]) #wyświetlenie 1 elementu z zagnieżdżonej listy

"""
Przy użyciu indeksowania można też podmieniać wartości. Zmiana dzieje się
momentalnie, nie trzeba nadpisywać"""
gniazdo[2] = "sraczka"
print(gniazdo)

"""Listy można dodawać do siebie (konkatenacja) i mnożyć"""

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

print(lista1 + lista2)

print(lista1 * 3)

"""
Listy mają specjalne funkcje i metody, takie jak:
"""
print( len(lista1) ) #od length, wyświetlenie długości (liczby elementów)
"""
Jaki będzie len(gniazdo)? 4 czy 6?
"""

print( min(lista1) ) #najmniejsza wartosc
print( max(lista1) ) #najwieksza wartosc
#tez dla stringowych wartości:

owoce = ["borowka", "gruszka", "ananas", "pomidor", "truskawka", "cukinia"]

print(min(owoce))
print(max(owoce))
# *Ciekawostka: kolejność wg ASCII

owoce.append("jablko") #dodawanie na koncu wartosci podanej w nawiasie
print(owoce)

"""
Przykładowa lista takich możliwości:
https://www.programiz.com/python-programming/methods/list
Warto zapoznać się chociaż z częścią, np. remove, count, index
i w razie potrzeby wyszukiwać - często daną operację, którą byśmy chcieli
zrobić, można wykonać za pomocą już istniejącej metody i tak jest łatwiej.

Można sprawdzać, czy dany element znajduje się w liście lub czy się w niej
nie znajduje za pomocą "in" i "not in" -> wynik: True albo False
"""

print( "borowka" in owoce ) #zwraca True
print( "ziemniak" in owoce ) #zwraca False

#analogicznie
print( "marchewka" not in owoce ) #zwraca True

"""
in i not in można wykorzystywać do konstruowania instrukcji z ifami, np.:
"""
if "pomidor" in owoce:
    print("Pomidor to też owoc, przynajmniej wg botaników")
