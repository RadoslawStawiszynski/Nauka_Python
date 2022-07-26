# IF
print('ZADANIE IF')

A = int(input("Wpisz liczbę A:"))
B = int(input('Wpisz liczbę B:'))
print("Teraz sprawdzę która liczba jest większa")
if A > B:
    print('Liczba A =', A, 'jest większa')
elif B > A:
    print('Liczba B =', B, 'jest większa')
else:
    print('Liczby są równe')

# Liczba minimalna
print()
print('ZADANIE - Znajdź liczbę minimalną')
L = [2, 5, 7, -3, 2, 4, -9, 0, 1, -18]
L2 = [32, 35, 33, -3, 22, 4, -3, 0, 1, -18]


def min_number(self):
    min_l = self[0]
    i = 0
    while i < len(self):
        if self[i] < min_l:
            min_l = self[i]
        else:
            i += 1
            pass
    print('Liczba minimalna wynosi:', min_l)


### Sortowanie liczb
print()
print('ZADANIE - Sortowanie liczb')


def sort_number(self):
    i = 0
    while i != len(self) - 1:
        if self[i] > self[i + 1]:
            self.append(self[i])
            del self[i]
            i = 0
        else:
            i += 1
            continue

    return self

