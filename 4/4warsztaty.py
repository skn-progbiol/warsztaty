"""Przypomnienie
1. typy danych i sprawdzanie ich
2. jak wygląda lista i co można z nią zrobić
3. ify i elsy
4. pętla while
5. pętla for
6. range()
7. funkcje"""

def funkcja1(parametr):  # DEFiniowanie funkcji - nadanie jej nazwy i określenie w nawiasie, co ta funkcja przyjmuje, jakie parametry
                         # parametry mogą być różne, np. stringi, listy, integery...
    print("To robi ta funkcja: " + parametr)  # ciało funkcji, czyli to, co funkcja ma zrobić

funkcja1("drukuje")  # wywołanie funkcji: hej, funkcjo1! weź to, co jest w nawiasie jako parametr i wykonaj na nim działanie


def funkcja2(parametr1, parametr2): #funkcje mogą przyjmować więcej niż jeden parametr
    print(parametr1 + parametr2)

funkcja2(2, 3) #wywołanie: hej, funkcjo2! weź 2 jako parametr1 i 3 jako parametr2 i wykonaj na nich działania


def funkcja3(): #mogą też nie przyjmować żadnych parametrów
  print("Nie ma parametru!")

funkcja3() #wywołanie


"""Zadanie: napisać funkcję, która będzie przyjmowała listę z nazwami zwierzątek. 
W środku funkcji lista ulubionych zwierzątek (ulubione). 
Jeśli zwierzątko należy do ulubionych, to ma zwrócić 'zwierzątko jest super', 
a jeśli nie to 'zwierzatko jest fuj' (zamiast 'zwierzątko' nazwa tego zwierzątka)"""

# rozwiązanie:
def ocena(lista_zwierzatek):
    # początek ciała funkcji (wszystko co jest w niej z wcięciem)
    ulubione = ["pyton", "piesek", "kotek"]
    for zwierzatko in lista_zwierzatek:
        if zwierzatko in ulubione:
            print(zwierzatko + " jest super")
        else:
            print(zwierzatko + " jest fuj")
    # koniec ciała funkcji

ocena(["pajak", "pyton", "papuga", "miś", "kotek"])

"""Komplikacja: w funkcji lista zwierząt z futerkiem (futerkowe). 
Zadanie: dopisać warunek, który sprawdzi, czy zwierzątko jest w ulubionych *i* w futerkowych. Wtedy wyświetlić 'zwierzatko jest super i ma futerko'"""

def ocena(lista_zwierzatek):
    ulubione = ["pyton", "piesek", "kotek"]
    futerkowe = ["piesek", "kotek", "miś"]
    for zwierzatko in lista_zwierzatek:

        if zwierzatko in ulubione and zwierzatko in futerkowe:  # ważne: and
            print(zwierzatko + " jest super i ma futerko")

        if zwierzatko in ulubione:
            print(zwierzatko + " jest super")
        else:
            print(zwierzatko + " jest fuj")

ocena(["pajak", "pyton", "papuga", "miś", "kotek"])

"""Na tym przykładzie możemy zapoznać się ze składnią 'and'. Podobnie jak językowe czy logiczne 'and' czy po polsku 'i' sprawia ono, że sprawdzane są 
dwa warunki jednocześnie: efektem jest True tylko jeśli oba są prawdziwe.
Np. dla pytona prawdziwym jest, że znajduje się w ulubione, ale już nie to, że znajduje się w futerkowe -> dlatego nie wykonuje się instrukcja 
wyświetlająca 'zwierzątko jest super i ma futerko'.
Kotek z kolei jest w obu listach, dlatego dla niego mamy True and True -> instrukcja z wyświetleniem wykonuje się."""

"""Widzimy jednak, że w przypadku kotka wyświetla się zarówno 'kotek jest super i ma futerko' i 'kotek jest super'. Po co się tak powtarzać, 
skoro Python umożliwia uniknięcie takiej sytuacji:"""

def ocena(lista_zwierzatek):
    ulubione = ["pyton", "piesek", "kotek"]
    futerkowe = ["piesek", "kotek", "miś"]
    for zwierzatko in lista_zwierzatek:
        if zwierzatko in ulubione and zwierzatko in futerkowe:
            print(zwierzatko + " jest super i ma futerko")

        elif zwierzatko in ulubione:  # ważne: elif
            print(zwierzatko + " jest super")

        else:
            print(zwierzatko + " jest fuj")

ocena(["pajak", "pyton", "papuga", "miś", "kotek"])

"""elif to zlepek powstały z połączenia 'else if'. Wykonuje on się tylko jeśli poprzedni warunek (albo żaden z poprzednich warunków) nie został spełniony. 
Warto popatrzeć tu: https://www.programiz.com/python-programming/if-elif-else 
W naszym przypadku wyszło to tak, że od góry do dołu sprawdzane były warunki dla kolejnych zwierzątek. W przypadku kotka sprawdzone zostało 
if zwierzatko in ulubione and zwierzatko in futerkowe, a skoro dało to True (kotek jest w obu listach), to następne warunki nie były już sprawdzane."""

"""elif ma sens np. kiedy mamy do czynienia z przedziałami liczbowymi. Weźmy funkcję dojrzalosc, która będzie przyjmować wiek."""

def dojrzalosc(wiek):

    if wiek < 18:        #jeśli wiek jest mniejszy niż 18
        print("niepełnoletni")

    elif 18 <= wiek < 65: #jeśli wiek jest większy lub równy 18, ale mniejszy od 65
        print("dorosły")

    else:                #jedyna inna ewentualność to wiek większy od 65
        print("starzec")

dojrzalosc(17)

"""Funkcja sprawdza, czy wiek jest mniejszy od 18. W naszym przypadku jest, więc wyświetla 'niepełnoletni'. Skoro wiemy już, 
że wiek jest mniejszy niż 18, to nie ma sensu sprawdzać czy mieści się w przedziale 18-65, ani 65+. Dlatego zastosowaliśmy elif."""

"""Weźmy inną funkcję (figury), która przyjmuje kształt i kolor."""

def figury(ksztalt, kolor):
    if ksztalt == "trojkat":
        print("Figura jest trojkatem")
    elif ksztalt == "kolo":
        print("Figura jest kolem")
    elif ksztalt == "kwadrat":
        print("Figura jest kwadratem")

    if kolor == "niebieski":
        print("Figura jest niebieska")
    elif kolor == "zielony":
        print("Figura jest zielona")
    elif kolor == "czerwony":
        print("Figura jest czerwona")

figury("trojkat", "zielony")

"""Tutaj zastosowaliśmy najpierw serię warunków if, elif, elif, bo jeżeli mamy do czynienia z jakimiś kształtem, 
to już na pewno nie mamy z innym (wykluczają się one wzajemnie), więc nie ma sensu sprawdzać wszystkich. 
Drugą serię warunków zaczynamy jednak znowu od if, bo istotne jest dla nas, żeby sprawdzona i wyświetlona została także informacja o kolorze. 
Gdybyśmy warunki związane z kolorem zaczęli od elif, to...




...sprawdzony byłby tylko kształt."""

"""Wróćmy do funkcji ze zwierzątkami. Mamy listę ulubione i futerkowe. Dodajmy jeszcze luskowe, dla zwierząt, które mają łuski. Dodajmy warunek, 
który sprawdzi czy dane zwierzątko ma futerko lub łuski."""

def ocena(lista_zwierzatek):
    ulubione = ["pyton", "piesek", "kotek"]
    futerkowe = ["piesek", "kotek", "miś"]
    luskowe = ["pyton", "sandacz", "t-rex"]

    for zwierzatko in lista_zwierzatek:
        if zwierzatko in ulubione and zwierzatko in futerkowe:
            print(zwierzatko + " jest super i ma futerko")

        elif zwierzatko in futerkowe or zwierzatko in luskowe:  # ważne: or
            print(zwierzatko + " ma futerko albo łuski")

        elif zwierzatko in ulubione:
            print(zwierzatko + " jest super")
        else:
            print(zwierzatko + " jest fuj")

ocena(["pajak", "pyton", "papuga", "miś", "kotek"])

"""Or to 'lub', czyli sprawdzamy, czy *chociaż jeden* z warunków został spełniony. Jeśli pierwszy jest True i/lub drugi jest True, 
to całość wychodzi też True, tak jak w przypadku pytona i misia. 
A dlaczego dla kotka wyświetla się tylko że jest super i ma futerko? 




Bo użyliśmy "elif"."""

"""Kolejna lista i kolejny warunek: sprawdzenie, czy zwierzątko jest ulubione i czy nie jest groźne."""

def ocena(lista_zwierzatek):
    ulubione = ["pyton", "piesek", "kotek"]
    futerkowe = ["piesek", "kotek", "miś"]
    luskowe = ["pyton", "sandacz", "t-rex"]
    grozne = ["pajak", "pyton", "miś"]

    for zwierzatko in lista_zwierzatek:

        if zwierzatko in ulubione and zwierzatko not in grozne:  # ważne: not in
            print(zwierzatko + " jest super i nie trzeba sie bac!")

        if zwierzatko in ulubione and zwierzatko in futerkowe:
            print(zwierzatko + " jest super i ma futerko")
        elif zwierzatko in futerkowe or zwierzatko in luskowe:
            print(zwierzatko + " ma futerko albo łuski")
        elif zwierzatko in ulubione:
            print(zwierzatko + " jest super")
        else:
            print(zwierzatko + " jest fuj")

ocena(["pajak", "pyton", "papuga", "miś", "kotek"])

"""Warunki już mamy przerobione. 
Spróbujmy sobie teraz wyświetlić naszą listę ulubione z funkcji ocena."""
print(ulubione)

"""Dostajemy błąd informujący, że zmienna ulubione nie została zdefiniowana. Dlaczego? 



Bo zmienna ulubione zawierająca listę znajduje się w ciele funkcji. To oznacza, że można z niej korzystać tylko *lokalnie* - jest zmienną *lokalną*. 
Nie można jej przywołać "z zewnątrz". 

Zapoznajmy się z kwestią zmiennych lokalnych ("wewnętrznych") i globalnych ("zewnętrznych", ogólno dostępnych) na kolejnych przykładach."""

"""Parametry lokalne nie moga byc przywolane z globalnego poziomu:"""
def humor():
    humorek = "10/10"
    print(humorek)
humor()

print(humorek)

"""Ale parametry globalne moga byc wywolane w funkcji"""
nastroj = '8/10'
def jaki_nastroj():
    print(nastroj)
jaki_nastroj()

"""Kolejna ważna sprawa: ostatnio wywoływaliśmy funkcję w niej samej (rekurencja), ale można też wywoływać jedną funkcję 
w drugiej funkcji, tak jak poniżej:"""
"""Jedna funkcja moze przywolywac druga"""
def jaki_humor():
    humor()
jaki_humor()

"""Jesli powstanie nowy parametr lokalny, to nadpisuje poprzedni"""
def smutek():
    humor()    #w funkcji humor mamy zdefiniowany humorek jako "10/10"
    humorek = '2/10'
    print(humorek)
smutek()

"""Co jesli taka sama nazwa parametru globalnego i lokalnego?"""
humorek = '5/10'
humor()

"""Zmienna lokalna jest niejako ważniejsza -> jeśli została zdefiniowana w jakiejś funkcji to funkcja ta będzie korzystać ze swojej zmiennej. 
Tak jak np. kiedy chcemy przedstawić w urzędzie projekt budżetu obywatelskiego Wrocławia, interesuje nas prezydent miasta, 
a nie prezydent Polski, ani tym bardziej innego miasta czy kraju."""

"""global -> informacja, że chcemy zmodyfikować zmienną globalną"""

humorek = "5/10"
def humor():

    global humorek

    humorek = "10/10"
    print(humorek)
humor()
print(humorek)

"""Tutaj w ciele funkcji daliśmy znać (za pomocą global), że to, co tu będziemy robić ze zmienną humorek ma mieć efekt globalny. 
I tak się stało, nawet kiedy spoza funkcji wykonujemy print(humorek), to wychodzi nam '10/10', a nie '5/10', jak wcześniej 
globalnie została zdefiniowana ta zmienna."""

"""Poprzednio już była mowa o tym, że kiedy korzystamy z print(), to uzyskujemy wyłącznie wyświetlenie jakiejś wartości. 
Natomiast jeśli chcemy, żeby nasza funkcja faktycznie coś *zwracała*, trzeba użyć *return*. Zobaczmy, dlaczego:"""

"""sprawdzenie typu"""
type(print("hello"))

"""Wychodzi nam NoneType, czyli kolejny typ danych, w którym jedyną możliwą jest None. None oznacza nic, brak, 
nie jest równoznaczne z zero -> nie ma to żadnej wartości z punktu widzenia komputera."""

"""Funkcja wykorzystujaca print tez zwraca None"""
type(humor())

"""Kiedy jest return, to zwracany jest konkretny typ danych"""
def humor():
    humorek = "10/10"
    return humorek

type(humor())

"""Po co to zwracanie? Np. funkcje moga sobie przekazywac wartosci"""
def dwa_do_drugiej():
    return 2*2             #funkcja zwraca po prostu wynik 2*2

def dwa_do_trzeciej():
    print(dwa_do_drugiej()*2) #funkcja wyświetla wynik z funkcji dwa_do_drugiej pomnożony razy 2

dwa_do_trzeciej()

"""Gdy zamiast return damy print w funkcji dwa_do_drugiej, to dostajemy błąd -> zwraca ona nic - None, więc 
dwa_do_trzeciej nie ma z czego korzystać"""
def dwa_do_drugiej():
    print(2*2)

def dwa_do_trzeciej():
    print(dwa_do_drugiej()*2) #funkcja wyświetla wynik z funkcji dwa_do_drugiej pomnożony razy 2

dwa_do_trzeciej()

"""Zadanie: problem Collatza
https://pl.wikipedia.org/wiki/Problem_Collatza
Napisz funkcję collatz, przyjmującą jeden parametr: liczba.
Jeżeli liczba jest podzielna przez 2, to niech collatz() wyświetli wynik dzielenia liczba//2 (//, czyli dzielenie bez reszty) 
i zwróci tę wartość (return) (wyświetli, żebyśmy widzieli, co się dzieje i zwróci, żeby przekazać dalej),
jeśli nie - niech wyświetli i zwróci 3 * liczba + 1.
Napisz drugą funkcję, która będzie przyjmowała input od użytkownika i przywoływała funkcję collatz() począwszy od tej liczby 
i będzie się wykonywała, aż dojdzie do 1."""

def collatz(liczba):
    if liczba % 2 == 0:  # jeśli jest parzysta
        a = liczba // 2  # to podziel bez reszty przez 2
        print(a)  # wyświetlenie
        return a  # zwrócenie

    else:  # w przeciwnym wypadku, czyli kiedy jest nieparzysta
        b = 3 * liczba + 1
        print(b)
        return b

def wprowadzenie():
    wpisana = int(input(
        "Podaj liczbe: "))  # wez input od uzytkownika i zamien go na integer (input zawsze jest stringiem, co byśmy nie wpisali)
    while collatz(wpisana) > 1:  # dopóki wynik z collatz() jest większy od 1
        wpisana = collatz(wpisana)  # obliczaj wynik z collatz i nadpisuj tym wynikiem zmienną wpisana

wprowadzenie()

"""Jakiej liczby byśmy nie wpisali, zawsze dojdziemy do 1!"""
