"""Simon Says

Exercises

1. Speed up tile flash rate.
2. Add more tiles.

Rule:-
1. first you have to start the game by tapping any tile.
2. Afterwards you just have to tap the tiles sequentially, in order as they blinks
"""

from random import choice
from time import sleep
from turtle import *
from freegames import floor, square, vector

pattern = []  #list for storing the patterns
guesses = []  #list for storing the guesses
tiles = {
    vector(0, 0): ('red', 'dark red'),  #setting the tile position & color
    vector(0, -200): ('blue', 'dark blue'),
    vector(-200, 0): ('green', 'dark green'),
    vector(-200, -200): ('yellow', 'khaki'),
}

def grid():  #function to draw the tiles
    "Draw grid of tiles."
    square(0, 0, 200, 'dark red')
    square(0, -200, 200, 'dark blue')
    square(-200, 0, 200, 'dark green')
    square(-200, -200, 200, 'khaki')
    update()

def flash(tile):  #for blinking the tiles
    "Flash tile in grid."
    glow, dark = tiles[tile]  # taking the tapped tile in glow and dark variables
    square(tile.x, tile.y, 200, glow)  #draw the respective tile by glow variable attributes
    update()  #updating the screen 
    sleep(0.5)  #delay time for blinking
    square(tile.x, tile.y, 200, dark)  #draw the respective tile by dark variable attributes
    update()
    sleep(0.5)

def grow():
    "Grow pattern and flash tiles."
    tile = choice(list(tiles))
    pattern.append(tile)

    for tile in pattern:
        flash(tile)

    print('Pattern length:', len(pattern))
    guesses.clear()

def tap(x, y):  
    "Respond to screen tap."
    onscreenclick(None)
    x = floor(x, 200)  #reconising the x coordinate of typed position
    y = floor(y, 200)  #reconising the y coordinate of typed position
    tile = vector(x, y)  #storing the coordinates to tile vector
    index = len(guesses)  #storing the length of the guesses list

    if tile != pattern[index]:  #If the your guessed tile not matching the pattern then exit the game
        exit()

    guesses.append(tile)  #storing your guess to the list
    flash(tile)  #after tapping the respective tile will flash

    if len(guesses) == len(pattern):  #calling grow function if both the list length will same
        grow()

    onscreenclick(tap)

def start(x, y):
    "Start game."
    grow()
    onscreenclick(tap)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()  #calling grid function that we made for drawing the tiles
onscreenclick(start) #calling start function upon tapping anywhere into the screen 
done()
