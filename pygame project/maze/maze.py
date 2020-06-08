"""Maze, move from one side to another.

Excercises

1. Keep score by counting taps.
2. Make the maze harder.
3. Generate the same maze twice.

"""

from turtle import *
from random import random
from freegames import line

def draw():  #After starting the project firstly this function will be called
    "Draw maze."
    color('black')
    width(5)

    for x in range(-200, 200, 40):
        for y in range(-200, 200, 40):
            if random() > 0.5:  #drawing the maze randomly
                line(x, y, x + 40, y + 40) #line function will draw the line from (x,y) to (x+40,y+40)
            else:
                line(x, y + 40, x + 40, y)

    update()  #for making updates into the screen

def tap(x, y):  #At every tap this function will be called
    "Draw line and dot for screen tap."
    if abs(x) > 198 or abs(y) > 198:  #checking if the tap is within the window or not.
        up()  #for pen up
    else:
        down()  #for pen down

    width(2)  #width of line
    color('red') #color of line
    goto(x, y)  #for going to the respective position where the user tapped
    dot(4)  #making dot where the user tapped

setup(420, 420, 370, 0)  #setting screen size
hideturtle()  #for hiding the turtle pointer
tracer(False)  #for changing the project state smoothly, try after removing it.
draw()  #calling function that we made earlier for dreawing the maze
onscreenclick(tap)  #On every tap into the window tap function will be called 
done()  #Terminating statement
