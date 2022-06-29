print('Przykład nr 1')
stopien = 0
zmeczenie = 0
brzydkapogoda = 0
while stopien < 101:
    print(stopien)
    if zmeczenie == True:
        break
    elif brzydkapogoda == True:
        break
    else:
        stopien = stopien + 1
print('Przykład nr 2')
x = 45
y = 50
while x < 50 and y < 100:
    x = x + 1
    y = y + 1
    print(x, y)

# while True:
#    kod kod kod kod kod kod
#    if warto == True:
#       break
print('Przykład nr 3')
n = int(input('Wpisz ile zrobisz kroków:'))+1
i = 0
while i < n:
    # będzie drukował tylko wartości podzielne przez dwa
    if i%2 == 0:
        print('Zrobiłeś teraz ', i, ' krok/-i/-ów.')
    else:
        pass # puszcza dalej nic nie robiąc
    i += 1
print('koniec wycieczki')

print('Przykład nr 4')
while True:
    if i % 177 == 0:
        print('Funkcja break zadziała na liczbie', i)
        break   # z uwagi na TRUE funkcja będzie wykonywana
        # tak długo aż znajdzie liczbę podzielną przez 17
    else:
        i += 1
        continue   # ten operator przenosi na początek funkcji IF
    # print('dalej w pętli') # ale nie wydrukuje tego
print('koniec wycieczki')
