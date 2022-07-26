# Sortowanie liczb
print('ZADANIE - Sortowanie liczb')
# pierwsza liczba jest większa od drugiej

L1 = [2, 5, 7, -3, 2, 4, -9, 0, 1, -8]
min_l = L1[0]
L2 = []


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


def sort_number(self):
    min_l = self[0]
    i = 0

    while i < len(self):
        if self[i] < min_l:
            min_l = self[i]
        else:
            i += 1
            pass
    print('Liczba minimalna wynosi:', min_l)


print(min_number(L1))
print(sort_number(L1))

'''
for i in L1:
    if i == dl_L - 1:
        i = 0
        print('Liczba minimalna wynosi:', min_l)
        continue
    elif L1[i] < min_l:
        min_l = L1[i]
        i += 1
        # L2.append[min_l]
    else:
        # L2.append[min_l]
        print("Koniec")

    # print(L2)
'''
