from random import randint
import math

# Game settings
game_width = 3
game_height = 3

# Generate random positions for the key and door
key_x = randint(0, game_width)
key_y = randint(0, game_height)

door_x = randint(0, game_width)
door_y = randint(0, game_height)

player_x = 0
player_y = 0

level = 0

steps = 0
distance_before_move = math.sqrt((key_x - player_x) ** 2 + (key_y - player_y) ** 2)

player_found_key = False

print("key: ", key_x, key_y)
print("door: ", door_x, door_y)

while not player_found_key:
    steps += 1
    print()
    print('''You can move in the directions [W/A/S/D]:
Press [Q] to quit the game.''')
    move = input("Where do you want to go?")
    match move.lower():
        case "w":
            player_y += 1
            if player_y > game_height:
                print("You have reached the top boundary of the board.")
                player_y = game_height
        case "a":
            player_x -= 1
            if player_x < 0:
                print("You have reached the left boundary of the board.")
                player_x = 0
        case "s":
            player_y -= 1
            if player_y < 0:
                print("You have reached the bottom boundary of the board.")
                player_y = 0

        case "d":
            player_x += 1
            if player_x > game_width:
                print("You have reached the right boundary of the board.")
                player_x = game_width
        case "q":
            print('Game over')
            quit()
        case _:
            print("I don't know where you want to go...")
            continue

    if player_x == key_x and player_y == key_y:
        print("Congratulations! You found the treasure! Now you can go open the door. The door is at ", door_x, "  ", door_y)
        text_1 = "You took %s steps."
        print(text_1 % steps)

    distance_after_move = math.sqrt((key_x - player_x) ** 2 + (key_y - player_y) ** 2)

    if distance_before_move > distance_after_move:
        print("You are closer to the key.")
    else:
        print("You are farther from the key.")

    distance_before_move = distance_after_move

    if player_x == door_x and player_y == door_y:
        print(f'Congratulations! You finished Level {level}.')
        level += 1
        quit()

    print(player_x, player_y)
