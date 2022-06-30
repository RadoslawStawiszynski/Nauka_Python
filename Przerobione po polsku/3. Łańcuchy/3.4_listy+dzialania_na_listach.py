# LISTA (ale pierwsze to łańcuch)#
str_wojownika_A = "miecz srebrzysty, sakiewka diamentów, " \
                    "buty samobiegi, peleryna supermena, tarcza Odyna, " \
                    "pierścień wspomnień, pukiel księżniczki"
print(str_wojownika_A)
print(str_wojownika_A[1])
print(type(str_wojownika_A))
print()
print()
lista_wojownika_1 = ["miecz srebrzysty", "sakiewka diamentów",
                     "buty samobiegi", "peleryna supermena", "tarcza Odyna",
                     "pierścień wspomnień", "pukiel księżniczki"]
print(lista_wojownika_1)
print(lista_wojownika_1[1])
print(type(lista_wojownika_1))
print()
print()
print(lista_wojownika_1[4])
print()
print()
lista_wojownika_1[4] = 'scyzoryk szwajcara'
print(lista_wojownika_1)

# Komentarz = 5 element listy zastąpiliśmy nowym elementem, innymi słowy zastąpiliśmy Odyna, scyzorykiem #
print()
print()
print(lista_wojownika_1[2:5])
print()
lista_liczb = [1, 2, 3, 5, 6, 8, 9]
print(lista_liczb)
print()
lista_mieszanka = [1, 'kolare', 2, 'koloru', 3, 'koralowego']
print(lista_mieszanka)
print()

# Poniżej dwie listy w jedną listę ###
lista_wojownika_1 = ["miecz srebrzysty", "sakiewka diamentów",
                     "buty samobiegi", "peleryna supermena", "tarcza Odyna",
                     "pierścień wspomnień", "pukiel księżniczki"]
lista_liczb = [1, 2, 3, 5, 6, 8, 9]
lista_z_list = [lista_wojownika_1, lista_liczb]
print(lista_z_list)
print()
print()
lista_liczb.append(10)
lista_liczb.append(13)
lista_liczb.append(15)
print(lista_liczb)
print()
del lista_liczb[2]
del lista_liczb[5]
print(lista_liczb)
print()
print()
# Działania arytemtyczne
lista_dodatnia = lista_liczb + lista_wojownika_1
print(lista_dodatnia)
print()
lista_mnozenia = lista_liczb * 5
print(lista_mnozenia)
# LUB
print(lista_liczb * 3)
# dzielenie i odejmowanie generują błędy, tak samo jak dodawanie liczb i odejmowanie
# można natomiast dodawać listy
print()
print()
# KROTKI
liczbaF = (0, 1, 1, 2, 3)
print(liczbaF)
print(type(liczbaF))
# LISTA i MAPA
ulubione_sporty = ['Lewandowski, Piłka Nożna',
                   'Gołota, Bokser',
                   'Piotr Żyła, Skoczek',
                   'Adam Małysz, Skoczek',
                   'Kubica, Kierowca bombowca']
print(ulubione_sporty)
print(type(ulubione_sporty))
print(ulubione_sporty[2])
# ... MAPA
ulubione_sporty_1 = {'Lewandowski': 'Płka Nożna',
                     'Gołota': 'Bokser',
                     'Piotr Żyła': 'Skoczek',
                     'Adam Małysz': 'Skoczek',
                     'Kubica': 'Kierowca bombowca'}
print(ulubione_sporty_1)
print(type(ulubione_sporty_1))
print(ulubione_sporty_1['Gołota'])
print()

del ulubione_sporty_1['Gołota']
print(ulubione_sporty_1)
ulubione_sporty_1['Kubica'] = "Kierowca rajdowy"
print(ulubione_sporty_1)
# Map nie można dodawać
