def test_zmiennych():
    pierwsza_zmienna = 10
    druga_zmienna = 20
    return pierwsza_zmienna * druga_zmienna


print(test_zmiennych())

# nie mozna wykonac kodu print(pierwsza_zmienna) bo nie ma tej zmiennej na zewnatrz def

inna_zmienna = 100


def test_zmiennych2():
    pierwsza_zmienna = 10
    druga_zmienna = 20
    return pierwsza_zmienna * druga_zmienna + inna_zmienna


print(test_zmiennych2())


# Pierwsza funkcja


def budowanie_statku(puszki):
    suma_puszek = 0
    for tydzien in range(0,500):
        suma_puszek = suma_puszek + puszki
        print('Tydzien %s = %s puszek zgniecionych' %(tydzien,suma_puszek))
        if suma_puszek >= 500:
            break
budowanie_statku(2)
print()
budowanie_statku(22)
