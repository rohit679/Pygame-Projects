"""Tiles, number swapping game.

Exercises

1. Track a score by the number of tile moves.
2. Permit diagonal squares as neighbors.
3. Respond to arrow keys instead of mouse clicks.
4. Make the grid bigger.

Rule:-
1. you can move only one tile at a time to the empty slot
2. Can you order the tiles 1 to 16 as follows
   1  2  3  4
   5  6  7  8
   9  10 11 12
   13 14 15 16

"""

from random import *
from turtle import *
from freegames import floor, vector

tiles = {}  #set for storing each and every tiles
neighbors = [          #setting neighbours for each tile can be only up,down,left,right.
    vector(100, 0),
    vector(-100, 0),
    vector(0, 100),
    vector(0, -100),
]

def load():
    "Load tiles and scramble."
    count = 1  #initializing the count number to assign to the tiles

    for y in range(-200, 200, 100):
        for x in range(-200, 200, 100):
            mark = vector(x, y)  #taking the position of each tile one by one 
            tiles[mark] = count  #storing the number into mark of each tile that is gonna draw at that tile
            count += 1  #increasing the count everytime

    tiles[mark] = None  #storing none to the last tile

    """for count in range(1000):
        neighbor = choice(neighbors)
        spot = mark + neighbor

        if spot in tiles:
            number = tiles[spot]
            tiles[spot] = None
            tiles[mark] = number
            mark = spot
"""
def square(mark, number):
    "Draw white square with black outline and number."
    up()
    goto(mark.x, mark.y)  #moving the pointer to the desired coordinates
    down()

    color('black', 'white')
    begin_fill()
    for count in range(4):  #making square tile
        forward(99)
        left(90)
    end_fill()

    if number is None:  #it may possible that you tapped wrong tile then the number will be none
        return
    elif number < 10:  #if the number is single digit then we have to move forward so that number will fill the tile properly
        forward(20)

    write(number, font=('Arial', 60, 'normal'))  #writing the number into the tile

def tap(x, y):
    "Swapping tile and empty square."
    x = floor(x, 100)
    y = floor(y, 100)
    mark = vector(x, y)  #storing the passed values into marks

    for neighbor in neighbors:
        spot = mark + neighbor  #finding the empty spot from neighours list.

        if spot in tiles and tiles[spot] is None:  #if the neighour of tile you pressed is empty then only we go for swapping
            number = tiles[mark]  #storing the tile mark number to the number variable
            tiles[spot] = number  #then we assign the number into the spot tile(empty tile)
            square(spot, number)  #calling square function for making square in spot position and fill the number
            tiles[mark] = None  #we assign the none into the mark tile(tile in which we tapped)
            square(mark, None)  #calling square function for making square in mark position and fill the number none

def draw():
    "Draw all tiles."
    for mark in tiles:
        square(mark, tiles[mark]) #calling square function by passing coordinates of tile & number 
    update()

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
load()  #calling the load function that we made
draw()  #calling the draw function that we made
onscreenclick(tap)
done()
