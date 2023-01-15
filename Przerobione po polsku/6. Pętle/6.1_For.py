print('Cześć')
print('Cześć')

print()

# LUB

for x in range(0, 2):
    print('Cześć2')
print()
for kruk in list(range(0, 3)):
    print('Cześć3')
print()
print(list(range(10, 20)))
print()

# inne możlwiości pętli for

for v in range(0, 5):
    print('Cześć %s' % v)
print()

liczba4 = 4
print('Cześć %s' % liczba4)
print()

# LISTA

lista_wojownika_1 = ["miecz srebrzysty", "sakiewka diamentów",
                     "buty samobiegi", "peleryna supermena", "tarcza Odyna",
                     "pierścień wspomnień", "pukiel księżniczki"]
for m_tydzien in lista_wojownika_1:
    print(m_tydzien)

# LUB

print()
print(lista_wojownika_1[3])
print()

# I

for m_tydzien in lista_wojownika_1:
    print(m_tydzien)
    print(m_tydzien)
print()

# I

lista_liczb = [1, 2, 3]

for m_tydzien in lista_liczb:
    print(m_tydzien)
    for w in lista_liczb:
        print(w,"a")
print()

# TEST
print('TEST')
print()
test = 20 + (10 * 365) - (3 * 52)
print(test)
print(20 + 10 * 365 - 3 * 52)

for dzien_o in range(0, 366):
    log = 20 + (dzien_o * 10)
    print("Monet %s" % log)
print()
print()
print()

for tydzien in range(1, 53):
    log = 20 + (tydzien * 70) - (3 * tydzien)
    print("Tydzień %s = %s" % (tydzien, log))
print()
print()
print()
for t in range(0, 53):
    for dtyg in range(1, 8):
        dzien_o = dtyg + t * 7
        if dzien_o <= 365:
            log = 20 + (dzien_o * 10) - (3 * t)
            tydzien = t + 1
            print("Tydzień %s dzień %s = %s" % (tydzien, dzien_o, log))
print()
print()
print()
for t in range(1, 54):
    tydzien = t
    dzien_o = t * 7
    if dzien_o <= 364:
        log = 20 + (dzien_o * 10) - (3 * t)
        print("Tydzień %s dzień %s = %s" % (tydzien, dzien_o, log))
    elif dzien_o >= 365:
        dzien_o = 365
        log = 20 + (dzien_o * 10) - (3 * t)
        print("Tydzień %s dzień %s = %s" % (tydzien, dzien_o, log))

# TEST 2 !!!!!!!!!!!!!!!!
print()
print(' TEST 2 ')
print()
print()
monety_poczatkowe = 20
m_tydzien = 70
kruk = 3
dzien_o = 365
monety = monety_poczatkowe
for tydzien in range(1, 54):
    if 1 <= tydzien < 53:
        monety = monety + m_tydzien - kruk
        print("Tydzień %s = %s" % (tydzien, monety))
    if tydzien == 53:
        monety = monety + 10
        print("Tydzień %s dzien %s= %s" % (tydzien, dzien_o, monety))


# ZADANIE 1 !!!!!!!!!!!!!!!!
print()
print('ZADANIE 1')
print()

L = []
for i in range(10):
    print(i+1)
    L.append(i**2)
print(L)

# ZADANIE 2 !!!!!!!!!!!!!!!!
print()
print('ZADANIE 2')
print()

T = {'wiśnia', '3.9', 'kompot'}
for t in T:
    print(t)
else:
    print('Koniec listy T')

# ZADANIE 3 !!!!!!!!!!!!!!!!
print()
print('ZADANIE 3')
print()

S = {'Renault': 2008, 'Mazda': 2020, 'Toyota': 2022}
for s in S:
    print(s, S[s])
else:
    print('Koniec listy Samochodów')