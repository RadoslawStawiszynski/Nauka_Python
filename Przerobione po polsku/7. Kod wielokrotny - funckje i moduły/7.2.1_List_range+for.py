# Lista z jednym argumentem

numbers = list(range(10))

print(numbers)
print(numbers[3])

# Lista z dwoma argumentami
numbers = list(range(10,16))

print(numbers)
print(numbers[3])

# Lista z trzema argumentami, skoki co 2

numbers = list(range(2, 20, 2))

print(numbers)
print(numbers[3])

# Lista z trzema argumentami v2

numbers = list(range(20, 1, -3))

print(numbers)
print(numbers[3])

# Tworzenie list z napisami
for i in range(5,11,2):
    print(str(i) + " hi")

# Listy kwadratowe
l_kwa = list(range(3,29))
print(l_kwa[4:7])
print(l_kwa[8:11])
