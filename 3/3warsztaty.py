'''
Podczas warsztatów omówiliśmy trzy ważne elementy programowania.
'range()', pętle 'for' i funkcje
Zacznijmy od pętli 'for'
'''

#Pętla for wygląda tak:
#Załóżmy, że chcemy wydrukować każdy element w osobnej linii. Gdybyśmy chceli to zrobić odnosząc sie do indexu
#to zajełoby to bardzo dużo miejsca, a co w sytuacji gdy mamy 100000 elementów? Więc możemy zrobić tak:

lista = [0,1,2,3,4,5]
for i in lista:
    print(i)

# dosłownie: dla każdego elementy listy lista wydrukuj go.
# for to pętla, czyli wykonuje obrót dla każego elementu listy.
# zmienna 'i' jest tymczasową zmienną w której dany element jest przechowywany przez TYLKO swój obrót.
# Czyli Pierwszy obrót: pierwsza wartość w liście to 0 więc pętla przypisuje wartość 0 do zmiennej 'i' i wykonuje
# wszystko co jest z wcięciem poniżej, czyli ją drukuje. Drugi obrót: przypisz wartość 1 do 'i' i wykonaj kod poniżej itd.

'''
range() to generuje kolejne liczby, 
jeśli chcemy uzyskać ciąg 1,2,3,4,5 możemy zamiast pisać liste [0,1,2,3,4,5] (możemy tak oczywiście robić,
ale co wtedy gdy mamy mieć ciąg złożony z 1000 liczb?) użyć range, który go wygeneruje. Wygląda to tak: 
'''
range(6)
#Kiedy przyjmuje tylko jeden arguemnt (tutaj 6) to będzie generować ciąg właśnie 0,1,2,3,4,5
#żeby to zobaczyć trzeba to puścić przez pętle for:
for i in range(6):
    print(i)

# Zaczyna o 0 i kończy na liczbie od 1 mniejszej niż podany arguemnt
# Jeśli podamy tylko jeden argument to jest to liczba przed którą powinna skończyć wyliczankę
# Jeśli podamy dwa:
range(3,9)
# to będzie wyliczać od 3 do liczby przed 9. 3,4,5,6,7,8
# Jeśli podamy 3.
range(2,11,2)
# to będzie wyliczać od 2 do 11, ale będzie przeskakiwać co dwie liczby,czyli : 2,4,6,8,10 itd.

#Zadanie: Napisz pętle for, która wyprintuje wartości od 1000, do 1049 przeskakując co 3.
#pętle for moją jeszcze dwa ważne elementy:
for i in range(10):
    if i == 3:
        continue
    if i ==5:
        break
    print(i)

print('koniec pętli')

# continue sprawia, że pętle ignoruje resztę danego obrotu i przechodzi do kolejnego elementu zbioru
# czyli nie wydrukuje 3 ponieważ funkcja print jest niżej, i przejdzie dalej do liczby 4, gdzie już wykona wszystko
# break zamyka pętle zanim skończy wyliczankę i wykona program poniżej bez wcięcia.

#Funkcje
#Funkcja jak funkcja w matematyce ma jakiś input i output jak y = x + 1
# x to input, wartość jaką dajemy do przemielenia
# y to output jaką dostajemy po przemieleniu
# przemielenie tutaj to dodanie do inputu wartości 1.
# Czyli jeśli input x = 10 to output y = 11
# Definiowanie funckji w pythonie to napisanie w nim wzoru (algorytmu)
# Funckja musi mieć nazwę (bo narazie tylko ją definiujemy, żeby jej użyć trzeba ją wywołać)
# Ile może przyjąć inputów (pod podstać zminnych) i co ma zwrócić
# Na przykładzie y = x + 1 wygląda to tak:
def działanie(x):
    y = x + 1
    return y
# Po 'def' nadajemy funkcji nazwę i w nawiasie zmienną, która będzie przyjmować input czyli x:
# Na końcu funkcja zwraca (do zmmiennej do której ją wywołaliśmy to co jest po 'return'
# Czyli
proste_działąnie = działanie(10)
# teraz proste_działanie ma wartość 11 bo do inputu 10 dodaliśmy 1 w definicji funkcji
# Zadanie: Napisz funckje, która będzie obliczała silnie ( np. 5! = 5*4*3*2*1; pamiętaj że 0! = 1)
