#Przypomnienie zmiennych

#zmienna to takie "pudlo" któremu nadajemy nazwę i do którego wsadzamy dane
#zmienna = dane --> stwórz zmienną i przypisz do niej jakieś dane
liczba = 10

#Zmienna oprócz samych danych zawiera w sobie też inne informacje, takie jak typ zmiennej, co umożliwia komputerowi 
#odpowiednią interpretację tych danych. Przykładowo, zmienna typu int wskazuje, że dane należy interpretować jako mówiące o liczbach
#całkowitych, a string - że dane należy interpretować jako znaki. 
#Dokładniej - string w Pythonie jest przeważnie kodowany w UTF-8, gdzie każdy znak (litery, cyfry itd.) jest zapisany w 1-3 bajtach (8-24 bitach)
#Int w Pythonie to po prostu liczba całkowita od -2^31 do 2^31 zapisana w binarnym, czyli ciąg 32 bitów. 

#Python jest w stanie automatycznie utworzyć zmienną danego typu na podstawie danych, które wpiszemy. 
#zmienna = 10 --> zmienna automatycznie staje się int
#zmienna = 'xd' --> zmienna automatycznie staje się string
#zmienna = [1, 2, 3] --> zmienna automatycznie staje się list

#Możemy jednak 'zmusić' Pythona, aby powstał taki typ zmiennej, jaki chcemy.
#Przypisujemy wtedy do zmiennej odpowiednią klasę (nie mylić z funkcjami, ale podobne)
#Przykładowe klasy to str() i int() które za argument przyjmują dane które mają znaleźć się w nowoutworzonej zmiennej
#Argumentem może też być zmienna innego typu i wtedy zostanie przeprowadzona konwersja jednego typu zmiennej w inny

x = str(liczba)
y = str('liczba')
z = liczba

print(x, y, z)
print(type(x), type(y), type(z))


#string jako coś podobnego do listy

#in sprawdza, czy w liście znajduje się jakiś element, a w przypadku stringa - czy w stringu znajduje się jakiś mniejszy string (substring)

zdanie = "bardzo długie zdanie"

print('bardzo' in zdanie)

#Tak samo jak w przypadku list, na stringu można przeprowadzić slicing wykorzystując string[start:end:step]
#W tym konkretnym przypadku zdanie[2] to 3 element stringa, czyli string 'j'

zdanie = "kajak"

print(zdanie[2])

#string można łatwo przekonwertować na list, w którym każdy element stringa stanie się elementem listy

lista_ze_zdania = list(zdanie)
print(lista_ze_zdania)

#po stringu możemy też iterować. Tutaj dla każdego elementu stringa printujemy go, czyli nasze zdanie zostanie przeliterowane
for i in zdanie:
  print(i)

#dzięki metodzie string.count(substring, start, end) możemy policzyć, ile razy w danym stringu występuje pewien ciąg znaków.
#możemy też wybrać, gdzie liczenie powinno się zacząć i skończyć.

dna = "ATGCCTGCAATC"

ilosc_G = dna.count('GC')
print(ilosc_G)

#string.replace(old, new, count) - NIE ZMIENIA pierwotnego stringa, zwraca nowy string, w którym pewien substring ('A') 
#został podmieniony na inny ('(adenina)'). Możemy też wybrać, ile razy ta podmiana ma nastąpić. Standardowo podmienia wszystko.


dna = "ATGCCTGCAATC"

dnax = dna.replace('A', '(adenina)')
print(dnax)

#Krótkie przypomnienie słowników: słownik = {key1: value1, key2: value2}, gdzie do kluczy key1 i key2 są przypisane wartości value1 i value2. 
#Aby dostać się do wartości w słowniku, piszemy np. słownik[key1] - to zwróci nam value1. 
#Kluczami i wartościami może być wszystko, od intów i stringów aż po funkcje. 
#Zmienić wartość pod kluczem możemy w ten sposób: dict[wybrany przez nas klucz] = (jakaś wartość, zmienna, funckja)
#Nowy klucz i wartość dodajemy podobnie: dict[nowy_klucz] = (jakaś wartość, zmienna, funkcja)

#Metoda str.maketrans(keys, values) zwraca słownik o kluczach keys i wartościach values. W naszym przypadku
#nasz słownik teoretycznie będzie wyglądać tak: {'A': 'T', 'T':'A'. 'G':'C', 'C':'G'}
#jednak zamiast stringów z literami będzie zawierał liczby, które odpowiadają dziesiętnemu zapisowi znaków tych liter z UTF-8
#Listę znaków i ich zapisów dziesiętnych można znaleźć tutaj: https://en.wikipedia.org/wiki/List_of_Unicode_characters
#Słownik nam posłuży do przekonwertowania ciągu nukleotydów z jednej nici na nuklotydy drugiej nici.

#Metoda str.translate(dict) Przyjmuje słownik zawierający klucze będące tym, co chcemy przetłumaczyć, oraz wartości, będącymi tym,
#na co chcemy przetłumaczyć. Zwraca przetłumaczony string, w tym przypadku DNA komplementarne.

dict_keys = "ATGC"
dict_vals = "TACG"

translation_table = str.maketrans(dict_keys, dict_vals)

dna = "ATGCCTGCAATCCTGATCCGTGTCAAGCT"

dna_complement = dna.translate(translation_table)
print(dna_complement)
print(translation_table)

#Przykład: Do jednego z kluczy ('T') w słowniku przypisujemy jakąś nową wartość. Teraz po zastosowaniu str.translate()
#'T' zostanie przetłumaczone na inny znak.

translation_table[65] = 123
dna_complement = dna.translate(translation_table)
print(dna_complement)

#Ze slownika za pomocą metod dict.keys(),  dict.values() i dict.items() możemy wyciągnąć klucze, wartości, oraz elementy, czyli klucze:wartosci
#Dla wygody można przypisać te wartości do listy. 

lista_kluczy = list(translation_table.keys())
print(lista_kluczy)
lista_wartosci = translation_table.values()
print(lista_wartosci)

#Operacje na plikach

#Do otwierania, modyfikowania, tworzenia i zapisywania plików stosujemy funkcję open(path, mode)
#path to ścieżka do pliku (np. w formie stringa). Na windowsie ważne upewnić się, że slash'e są "/" a nie "\". 
#mode to tryb działania. Podajemy go w formie np. mode='w', albo samo 'w'
#mode='w' --> Jeśli nie ma pliku podanego w path, to tworzy go, a jak jest, to kasuje całą jego zawartość.
#Umożliwia zapisanie danych w pliku
#mode='r' --> Działa tylko wtedy, jeśli plik podany w path istnieje, nie zmienia jego zawartości, tylko odczytuje.
#mode='x' --> Zwraca błąd jeśli plik podany w path istnieje, a jeśli nie istnieje, to go tworzy.
#mode='a' --> Jeśli nie ma pliku podanego w path, to tworzy go, a jak jest, to odczytuje plik i daje nam możliwość
#dodawania danych na końcu pliku. Skojarzenie - list.append()

#Aby stworzyć nowy plik możemy wykorzystać mode 'w', 'x' i 'a'. 
#Tworzymy i otwieramy plik za pomocą open() i przypisujemy go do zmiennej.
#Rozszerzenie pliku nie gra dla nas teraz istotnej roli, więc może być dowolne. 
#Wykorzystując open().write(string) możemy wpisać coś do naszego pliku. 
#Aby zamknąć plik i zapisać, wykorzystujemy open.close()

plik = open("C:/Users/xd/nowy_plik.xd", mode='w')
plik.write("To jest nowy plik")
plik.close()

#Aby odczytać dane z pliku możemy wykorzystać mode 'r'
#Otwieramy plik (tym razem już istniejący, np. plik FASTA ściągnięty z NCBI) za pomocą open()
#Dane z pliku odczytujemy za pomocą open().read() i zapisujemy je w zmiennej.
#Następnie zamykamy plik.

gen = open("C:/Users/xd/oksydaza.fasta", mode='r')
gen_string = gen.read()
gen.close()

#Aby sprawdzić, czy odczytaliśmy dane z pliku, możemy wyprintować naszą zmienną

print(gen_string)
print(gen_string.count('\n'))

#Wiele plików, w tym pliki FASTA zawierają '\n', czyli znak mówiący o wystąpieniu nowej linijki. 

zdanie = "halo \n xddd"
print(zdanie)

#Jeśli chcemy 'oczyścić' nasz plik FASTA, pozbyć się znaków nowej linijki i nagłówka, możemy napisać funkcję.

def oczysc_fasta(fasta): #Nasza funkcja przyjmuje jeden argument - fasta, czyli string który nam powstał po odczytaniu pliku FASTA
  
  if fasta[0] == '>':    #Najpierw możemy sprawdzić, czy nasz plik zawiera nagłówek FASTA, który zaczyna się od '>'. 
    fasta = fasta[fasta.index('\n'):]  #Jeśli tak, to usuwamy go. Do naszej zmiennej fasta przypiujemy fragment naszego pliku, 
                                       #który zaczyna się w miejscu, gdzie nagłówek się kończy, czyli w pozycji pierwszego '\n' w pliku, a kończy się normalnie.
                                       #fasta.index('\n') zwraca indeks pierwszego napotkanego '\n'.                                      
  fasta = fasta.replace('\n', '')      #Następnie zamieniamy każde '\n' na '', czyli nic (to nie spacja)
  return(fasta)   #Funkcja zwraca oczyszczoną fasta
  
#Po oczysczeniu możemy tą sekwencję zapisać.

gen_oczyszczony = open("C:/Users/xd/czyste.niefasta", mode='w')
gen_oczyszczony.write(oczysc_fasta(gen_string))
gen_oczyszczony.close()



#Znajdowanie częstości słów w tekście
#Funkcja, która przyjmuje jakiś tekst oraz słowo i zwraca, czy i ile razy dane słowo wystąpiło w tekście. 
#Oproćz tego może zwrócić posortowaną listę najczęstrzych słów.

def czestosc_slow(tekst, wybrane_slowo = 0): #wybrane_slowo = 0 --> to znaczy, że jesli podczas wywoływania funkcji nie podamy wybrane_slowo, to wybrane_slowo przyjmie wartosc 0
  
  #niedozwolone to słownik zawierający klucze będące zapisem w UTF-8 różnych znaków, takich jak , ? ! . itd. z wartościami None
  #Posłuży do usunięcia tych znaków z tekstu, aby 'słowo' i 'słowo!' nie były rozpoznawane jako różne słowa.
  niedozwolone = {33 : None, 34 : None, 39 : None, 40 : None, 41 : None, 42 : None, 44 : None, 45 : None, 46 : None, 47 : None, 58 : None, 59 : None, 63 : None}  
  
  #tekst oczyszczamy. Metody często można ze sobą łączyć - str.metoda1().metoda2().metoda3()
  #W tym przypadku stosujemy str.translate() dzięki któremu zastępujemy rózne znaki niczym,
  #str.replace() którym zastępujemy duzy myślnik i znak nowej linii (ale można to też wpisać w słownik),
  #oraz str.lower(), co zamienia wszystkie duże litery na małe.
  oczyszczony_tekst = tekst.translate(niedozwolone).replace('—', ' ').replace('\n', ' ').lower()
  
  #Do zmiennej slowa przypisujemy wynik string.split(), która tworzy listę stringów powstałą z rodzielenia jednego stringa. 
  #Działanie: "przyklad do rozdzialu" --> ["przyklad", "do", "rozdzialu"]
  # do split() możemy wykorzystać też argument sep=' ' (split(sep=' ')). 
  #Zmieniając string, który jest w sep, możemy zmienić po czym mamy rodzielać. Domyślnie spacja. 
  slowa = oczyszczony_tekst.split()

  #Tworzymy pusty słownik, do którego będziemy zapisywać słowa i ich częstości
  czestosc = {}
  
  #Lecimy po kolei po wszystkich słowach które mamy 
  for slowo in slowa:
    
    #jeśli słowo nie jest w słowniku, to zapisujemy je w nim i dajemy mu wartość 1
    if slowo not in czestosc:
      czestosc[slowo] = 1
    
    #A jeśli jest, to zwiększamy wartość o 1
    else:
      czestosc[slowo] = czestosc[slowo] + 1
  
  #Jeśli nie podano wybrane_slowo, to zwracamy słowa i ich częstości od największej wartości
  if wybrane_slowo == 0:
    return(sorted(czestosc.items(), key=lambda x: x[1])[::-1])
    
    #Dokładne wytłumaczenie powyższego return()
    #return() --> zwracamy (czyli jeśli mamy zmienna = funkcja(x), to w zmiennej będzie zawartość return. 
    #W tym przypadku zwracamy:
    #sorted(lista, key)[::-1] --> sorted zwraca posortowaną listę elementów wg klucza (key). [::-1], bo sorted zwraca od najmniejszego, a my chcemy na odwrót
    #jako lista dajemy czestosc.items(), czyli elementy słownika (pary klucz:wartość). 
    #key - klucz mówiący, jak posortować elementy. W naszym przypadku jest to lambda x: x[1]
    #lambda to funkcja. lambda x: x[1] --> Przyjmuje argument x i zwraca x[1]. W naszym przypadku x to kolejne elementy słownika.
    #x[1] oznacza wartość w parze klucz:wartość. Zatem nasz sorted() będzie sortował elementy słownika wg wartości. 
    
  
  #Jeśli wybrane_slowo jest w słowniku, to printujemy je oraz ile razy występuje w słowniku
  elif wybrane_slowo in czestosc:
    print(wybrane_slowo, "występuje tyle razy:", czestosc[wybrane_slowo])
  
  #Jeśli wybrane_slowo to nie 0 ani nie ma go w słowniku, to printujemy, że brak takiego słowa.
  else:
    print("Brak takiego słowa")
     


bible = open("C:/Users/thead/bible.txt", mode='r')
bible_text = bible.read()
bible.close()

#Przykład zastosowania tej funcji. Powinno wyjść 55
czestosc_slow(bible_text, 'satan')
