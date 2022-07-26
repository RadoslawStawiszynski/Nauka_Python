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
    x = ("Liczba minimalna wynosi:", min_l)
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


'''
i = 0
while i != len(L1)-1:
    if L1[i] > L1[i+1]:
        L1.append(L1[i])
        del L1[i]
        i = 0
    else:
        i += 1
        continue

print(L1)

'''







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



name = input("Enter Your Name:")

print("Hello " + name)
print("Get ready!!")
print()
time.sleep(1)

print("Let us play find a letter!!")
sleep(0.5)

word = "Flower"
wrd = ''
chance = 10

while chance > 0:
    failed = 0
    for char in word:
        if char in wrd:
            print(char)
        else:
            print("_")
            failed += 1
    if failed == 0:
        print("You Won!!Congratulations!!")
        break

    guess = input("Guess a Letter:")
    wrd = wrd + guess

    if guess not in word:
        chance -= 1
        print("Wrong Guess! Try Again")
        print("You have", + chance, 'more turn')
        if chance == 0:
            print("You Lose! Better Luck Next Time")'''