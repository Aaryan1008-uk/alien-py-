from turtle import Screen

import pgzrun 
from random import randint 

TITLE = "good shot"

WIDTH = 500
HEIGHT = 500


message = " " 


alien = Actor('alien')

def draw():
    screen.clear()
    screen.fill(color = (128,0,0))
    screen.draw.text(message, center = (400, 10), fontsize = 30)
    alien.draw()

def place_alien():
    alien.x = randint(50, WIDTH-50)
    alien.y = randint(50, WIDTH-50)

def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos):
        message = "good shot"
        place_alien()
    else:
        message = "You missed :)"



place_alien()
pgzrun.go()

