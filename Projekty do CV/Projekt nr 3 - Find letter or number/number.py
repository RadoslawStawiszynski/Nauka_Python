import random

print()
print('Przykład')
print()
print('Zgadnij jaka to liczba !? \n'
      'Masz 3 strzały aby odgadnąć liczbę między 1 a 12.\n'
      'Powodzenia !\n')

number = int(random.randint(1, 12))
chance = 3
print(number)


while chance > 0:
    guess = int(input("Podaj liczbę: "))
    chance -= 1
    if guess == number:
        print('BRAWO!!! odgadłeś liczbę')
        break
    elif guess not in range(1, 13):
        print("Liczba spoza zakresu szukanych liczb. Spróbuj jeszcze raz")
        chance += 1
    elif guess > number:
        print("Za duża number.")
    elif guess < number:
        print('Za mała number.')
    else:
        print('uwaga!błąd!')
        break

    if chance == 0:
        print("Wykorzystałeś wszystkie strzały!\n"
              "G A M E   O V E R")

