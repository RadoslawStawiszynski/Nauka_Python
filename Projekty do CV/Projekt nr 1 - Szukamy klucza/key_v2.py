import turtle
import pygame

# Ustawienie okna
window = turtle.Screen()
window.title("Moja Gra")
window.bgcolor("white")

# Stworzenie obiektu turtle
pen = turtle.Turtle()
pen.speed(0)  # Ustawienie prędkości rysowania

# Funkcja do rysowania planszy
def draw_board():
    for _ in range(4):
        pen.forward(200)
        pen.left(90)

# Wywołanie funkcji rysującej planszę
draw_board()

# Zamknięcie okna po kliknięciu
turtle.done()