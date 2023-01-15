# Sortowanie liczb
print('ZADANIE - Sortowanie liczb')
# pierwsza liczba jest większa od drugiej

L1 = [2, 5, 7, -3, 2, 4, -9, 0, 1, -8]
min_l = L1[0]
L2 = [32, 35, 33, -3, 22, 4, -3, 0, 1, -18]


def min_number(Ln):
    min_l = Ln[0]
    i = 0
    while i < len(Ln):
        if Ln[i] < min_l:
            min_l = Ln[i]
        else:
            i += 1
            pass
    x = f"Liczba minimalna wynosi: {min_l}"
    return x


def sort_number(Ln):
    i = 0
    while i != len(Ln) - 1:
        if Ln[i] > Ln[i + 1]:
            Ln.append(Ln[i])
            del Ln[i]
            i = 0
        else:
            i += 1
            continue

    return(Ln)

def selection_sort(y):
    for i, n in enumerate(y):
        j, m = min(enumerate(y[i:]), key = lambda a: a[1])
        y[j + i], y[i] = n, m
    return y

d = L2
print(selection_sort(d))

print(min_number(L2))
print(sort_number(L2))

