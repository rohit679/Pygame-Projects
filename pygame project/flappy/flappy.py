"""Flappy, game inspired by Flappy Bird.

Exercises

1. Keep score.
2. Vary the speed.
3. Vary the size of the balls.
4. Allow the bird to move forward and back.

"""

from random import *
from turtle import *
from freegames import vector

bird = vector(0, 0)  #setting initial position of the bird
balls = []  #list for storing the obstacle balls

def tap(x, y):
    "Move bird up in response to screen tap."
    l = vector(0, 30) #setting the new bird position
    bird.move(l)  

def inside(point):
    "Return True if point on screen."
    return -200 < point.x < 200 and -200 < point.y < 200

def draw(alive):
    "Draw screen objects."
    clear()  #clearing the window for drawing from fresh

    goto(bird.x, bird.y) #firstly move to the bird position and then draw the dot.

    if alive:
        dot(10, 'green')  #for drawing bird at new position if it's alive
    else:
        dot(10, 'red')  #for drawing the bird when it's collided with something

    for ball in balls:  #for drawing the balls at the respective positions
        goto(ball.x, ball.y)
        dot(20, 'black')

    update()

def move():
    "Update object positions."
    bird.y -= 5  #for moving the bird down continuously

    for ball in balls:
        ball.x -= 3  #for moving every ball left side continuously

    if randrange(10) == 0:  #for generating new balls into the screen
        y = randrange(-199, 199)  #for setting the hight of ball into screen
        ball = vector(199, y) 
        balls.append(ball)  #storing the ball into the list

    while len(balls) > 0 and not inside(balls[0]): #removing each ball when crossing the screen
        balls.pop(0)

    if not inside(bird):  #checking the ball not touching the screen walls
        draw(False)
        return

    for ball in balls:  #checking if the bird is collided by any ball
        if abs(ball - bird) < 15:
            draw(False)
            return

    draw(True)
    ontimer(move, 10) #setting the delay time of balls

setup(420, 420)
hideturtle()
up()  
tracer(False)
onscreenclick(tap)
move() # calling move function that we made earlier 
done()
