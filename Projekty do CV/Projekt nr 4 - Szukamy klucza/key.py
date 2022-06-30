from random import randint
import math

# from math import sqrt


game_width = 3
game_height = 3

key_x = randint(0, game_width)
key_y = randint(0, game_height)

door_x = randint(0, game_width)
door_y = randint(0, game_height)

# różne poziomy gry można stworzyć

player_x = 0
player_y = 0

level = 0

steps = 0
distance_before_move = math.sqrt((key_x - player_x) ** 2 + (key_y - player_y) ** 2)

player_found_key = False

print("klucz ", key_x, key_y)
print("drzwi ", door_x, door_y)

while not player_found_key:
    steps += 1
    print()
    print('''Możesz udać się w kierunkach określonych jako [W/A/S/D]: 
Aby opuścić grę wciśnij [Q]''')
    move = input("Dokąd chcesz iść?")
    match move.lower():
        case "w":
            player_y += 1
            if player_y > game_height:
                print("Doszedłeś do górnej granicy planszy.")
                player_y = game_height
        case "a":
            player_x -= 1
            if player_x < 0:
                print("Doszedłeś do lewej granicy planszy.")
                player_x = 0
        case "s":
            player_y -= 1
            if player_y < 0:
                print("Doszedłeś do dolnej granicy planszy.")
                player_y = 0

        case "d":
            player_x += 1
            if player_x > game_width:
                print("Doszedłeś do prawej granicy planszy.")
                player_x = game_width
        case "q":
            print('Game over')
            quit()
        case _:
            print("Nie wiem dokąd chcesz iść ...")
            continue

    if player_x == key_x and player_y == key_y:
        print("Gratulacje znalazłeś skarb! Teraz możesz iść otworzyć drzwi. Drzwi są  ", door_x, "  ", door_y)
        text_1 = "Zrobiłeś %s kroków."
        print(text_1 % steps)

    distance_after_move = math.sqrt((key_x - player_x) ** 2 + (key_y - player_y) ** 2)

    if distance_before_move > distance_after_move:
        print("Jesteś bliżej klucza.")
    else:
        print("Jesteś dalej od klucza.")

    distance_before_move = distance_after_move

    if player_x == door_x and player_y == door_y:
        print(f'Congratulation! You finished the Level {level}.')
        level += 1
        quit()

    print(player_x, player_y)
