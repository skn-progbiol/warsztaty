"""Zadanie: utworzenie klasy Urodziny, której artybutami są imię solenizanta, lista gości (słownik 
z imionami i adresami mejlowymi), budżet na zakupy i treść zaproszenia. Napisanie metod:   
	1. wyświetlająca czyje to urodziny;
	2. wyświetlająca imiona gości;
	3. wyświetlająca zaproszenie do konkretnej osoby z jego treścią;
	4. wyświetlająca kwotę do złożenia się przypadającą na gościa"""

"""Tworzenie klasy Urodziny - nazwy klas warto pisać z dużej litery, żeby od razu było wiadomo (np. dla innego programisty), że to klasa"""
class Urodziny():

"""Tworzenie konstruktora klasy, czyli takiej funkcji, która w przypadku tworzenia instancji (obiektu)
zainicjalizuje wszystkie atrybuty klasy - w tym przypadku imie solenizanta, listę gości, budżet na zakupy
i treść zaproszenia"""
    def __init__(self,imie_sol,lista_gosci,zakupy,tresc_zapr):
"""W ten sposób Python wie, że np. imie_sol odnosi się do własnego (self) atrybutu tej klasy"""
        self.imie_sol = imie_sol
        self.lista_gosci = lista_gosci
        self.zakupy = zakupy
        self.tresc_zapr = tresc_zapr

    def wyswietl_solenizanta(self):
"""Nazwy metod i funkcji w ogóle warto zaczynać małą literą"""
        print("To są urodziny ", self.imie_sol)

    def wyswietl_liste_gosic(self):
        print(self.lista_gosci.keys())

    def wyslij_zaproszenie_(self):
        for i,s in self.lista_gosci.items():
            print('Do ',i ,'(',s,')')
            print(self.tresc_zapr)

    def srednia_na_goscia(self):
        return self.zakupy/len(self.lista_gosci)

"""Tworzenie instancji (obiektu) klasy Urodziny o nazwie urodziny_krzysia. Przy tej operacji uruchamiana jest właśnie metoda __init__ -> następuje inicjalizacja"""
urodziny_krzysia = Urodziny('Krzysiek',
                            {'Marta':'marta@wp.pl',
                             'Kasia':'kasia@wp.pl'},
                            57,
                            'Zapraszam Cię serdecznie!'
                            )

"""Wywołanie metody wyswietl_solenizanta"""
urodziny_krzysia.wyswietl_solenizanta()

urodziny_krzysia.wyswietl_liste_gosic()

urodziny_krzysia.wyslij_zaproszenie_()

"""Metoda srednia_na_goscia nic nie wyświetla, tylko zwraca wartość (return, nie print). Dlatego jeśli chcemy zobaczyć wynik, musimy to zrobić w ten sposób:"""
kwota_na_os = urodziny_krzysia.srednia_na_goscia()
print(kwota_na_os)
