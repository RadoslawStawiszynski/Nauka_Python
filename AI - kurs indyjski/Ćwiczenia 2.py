# Sortowanie liczb
print('ZADANIE - Sortowanie liczb')
# pierwsza liczba jest większa od drugiej

L1 = [2, 5, 7, -3, 2, 4, -9, 0, 1, -8]
min_l = L1[0]
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
    x = f"Liczba minimalna wynosi: {min_l}"
    return x


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

    return(self)


print(min_number(L1))
print(sort_number(L2))
