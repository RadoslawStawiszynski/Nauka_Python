import random
# funkcja sprawdza długość łańcucha

print('nr1')
x = len("to jest długi łańcuch testowy")
print(x)
print('nr2')
z = len('0123')
print(z)

print('nr3')
lista_stworow = ['cyklop', 'meduza', 'elf', 'smok', 'trol', 'tarantula', 'ogr']
print(len(lista_stworow))

mapa_wrogow = {'Batman': 'Joker',
               'Superman': 'Lex Luthor',
               'Spiderman': 'Zielony Goblin'}

print('nr4')
print(len(mapa_wrogow))

print('Przykład')
owoc = ['jablko', 'pomarańcza', 'morela', 'agrest', 'awokado', 'mandarynka']
dlugosc = len(owoc)

for x in range(0, dlugosc):
    print(f'owoc pod indeksem {x} to {owoc[x]}')

print()
# funkcja min i max zwraca najmniejsą i najwiekszą wartość lub liczbę znaków
print('nr5')
ls = ['12', '23', '45', '67', '54', '32', '21', '21', '21']

print('max = ', max(ls))
print('min = ', min(ls))

# w stringach zwraca literę liczbę na której pozycji znajduje się dana litera
print('nr6')
ls_text = "K,R,ó,T,K,I,_,ła,ń,c,u,c,h,c"
print('max = ', max(ls_text), ' , numer pozycji = ', ord(max(ls_text)))
print('min = ', min(ls_text), ' , numer pozycji = ', ord(min(ls_text)))
# print(max('K,Ro,T,K,I,_,ł,a,ń,c,u,c,h'))

print()
print('Przykład')
print()
print('Zgadnij jaka to number !? \n'
      'Masz 3 strzały aby odgadnąć liczbę między 1 a 12.\n'
      'Powodzenia !\n')

liczba = int(random.randint(1, 12))
strzal = 3
print(liczba)


while strzal > 0:
    traf = int(input("Podaj liczbę: "))
    strzal -= 1
    if traf == liczba:
        print('Brawo odgadłeś liczbę')
        break
    elif traf not in range(1,13):
        print("Liczba spoza zakresu szukanych liczb. Spróbuj jeszcze raz")
        strzal +=1
    elif traf > liczba:
        print("Za duża number.")
    elif traf < liczba:
        print('Za mała number.')
    else:
        print('uwaga!błąd!')
        break

    if strzal == 0:
        print("Wykorzystałeś wszystkie strzały!\n"
              "G A M E   O V E R")


print()
print('nr7')
prices = {"banana": 1.20,
          "pineapple": 0.89,
          "apple": 1.57,
          "grape": 2.45,}
print(min(prices))
print(max(prices))

