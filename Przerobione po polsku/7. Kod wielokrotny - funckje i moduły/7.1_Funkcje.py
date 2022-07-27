# Funkcje range i list

print(list(range(1, 51)))


def funkcjaTestowa(mojeimie):
    print('Nazywam się %s' % mojeimie)


funkcjaTestowa('Radosław')
funkcjaTestowa('Agata')


def funkcjaTestowa2(imie, nazwisko):
    print('Nazywam się %s %s' % (imie, nazwisko))


funkcjaTestowa2('Radosław', 'Stawiszyński')

# Kolejne budowanie funkcji

imie = 'Robin'
nazwisko = 'Hood'
funkcjaTestowa2(imie,nazwisko)

# Kolejne budowanie funkcji

def oszczednosci(kieszonkowe,praca,wydatki):
    return kieszonkowe+praca+wydatki

print(oszczednosci(10,230,130))