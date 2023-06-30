import turtle
from random import randint
import math

# The GAME class
class Game:
    # Generate random positions for the key and door
    # Game settings
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.level = 0
        self.steps = 0
        self.steps_max = 15
        self.player_found_key = False
        self.player_x = 0
        self.player_y = 0
        self.key_x = randint(0, self.width)
        self.key_y = randint(0, self.height)
        self.door_x = randint(0, self.width)
        self.door_y = randint(0, self.height)
        self.distance_before_move = math.sqrt((self.key_x - self.player_x) ** 2 + (self.key_y - self.player_y) ** 2)
        self.distance_after_move = 0

        # Initialize Turtle screen and player
        self.screen = turtle.Screen()
        self.player = turtle.Turtle()
        self.player.shape("turtle")
        self.player.penup()

        # Calculate scale for drawing
        self.scale_x = self.screen.window_width() / self.width
        self.scale_y = self.screen.window_height() / self.height

    # Defining the goals of the game/level
    def start(self):
        self.draw_board()

        while self.steps < self.steps_max:
            print('''You can move in the directions [W/A/S/D]: \n Press [Q] to quit the game.''')
            move = input(f"You have left {self.steps_max-self.steps} steps. Where do you want to go? ")
            self.steps += 1
            self.move_player(move.lower())
        while self.steps == self.steps_max:
            print("GAME OVER")
            self.screen.bye()

    # Defining player moves
    def move_player(self, move):
        # W A S D moves
        match move.lower():
            case "w":
                self.player_y += 1
                if self.player_y > self.height:
                    print("You have reached the top boundary of the board.")
                    self.player_y = self.height
                    self.steps -= 1
            case "a":
                self.player_x -= 1
                if self.player_x < 0:
                    print("You have reached the left boundary of the board.")
                    self.player_x = 0
                    self.steps -= 1
            case "s":
                self.player_y -= 1
                if self.player_y < 0:
                    print("You have reached the bottom boundary of the board.")
                    self.player_y = 0
                    self.steps -= 1
            case "d":
                self.player_x += 1
                if self.player_x > self.width:
                    print("You have reached the right boundary of the board.")
                    self.player_x = self.width
                    self.steps -= 1
            case "q":
                print('Game over')
                self.screen.bye()
            case _:
                print("I don't know where you want to go...")
                self.steps -= 1

        # Middle ending game - Get KEY
        if self.player_x == self.key_x and self.player_y == self.key_y:
            print("Congratulations! You found the treasure! Now you can go open the door.")
            print(f'You took {self.steps} steps.')
            self.player_found_key = True

        # Logic of the moves
        self.distance_after_move = math.sqrt((self.key_x - self.player_x) ** 2 + (self.key_y - self.player_y) ** 2)

        # Hints for the full game
        while True:
            if self.player_found_key == False:
                goal = "key"
            else:
                goal = "door"

            if self.distance_before_move > self.distance_after_move:
                print(f"You are closer to the {goal}.")
            else:
                print(f"You are farther from the {goal}.")
            break

        self.distance_before_move = self.distance_after_move

        # Last ending game/level
        if self.player_x == self.door_x and self.player_y == self.door_y and self.player_found_key == True:
            print("x =", self.player_x, " y =", self.player_y)
            print(f'Congratulations! You finished Level {self.level}.')
            print(f'You took {self.steps} steps.')
            self.level += 1
            self.screen.bye()

        print("x =", self.player_x, " y =", self.player_y)
        self.update_player_position()

    # Update player position on the screen
    def update_player_position(self):
        x = self.player_x * self.scale_x - self.screen.window_width() / 2 + self.scale_x / 2
        y = self.player_y * self.scale_y - self.screen.window_height() / 2 + self.scale_y / 2
        self.player.goto(x, y)

    # Draw the initial board
    def draw_board(self):
        turtle.setworldcoordinates(0, 0, self.screen.window_width(), self.screen.window_height())

        for x in range(self.width + 1):
            turtle.penup()
            turtle.goto(x * self.scale_x - self.screen.window_width() / 2, -self.screen.window_height() / 2)
            turtle.pendown()
            turtle.goto(x * self.scale_x - self.screen.window_width() / 2, self.screen.window_height() / 2)

        for y in range(self.height + 1):
            turtle.penup()
            turtle.goto(-self.screen.window_width() / 2, y * self.scale_y - self.screen.window_height() / 2)
            turtle.pendown()
            turtle.goto(self.screen.window_width() / 2, y * self.scale_y - self.screen.window_height() / 2)

        self.update_player_position()

# Create a game instance and start the game
game = Game(3, 3)
game.start()
turtle.done()
