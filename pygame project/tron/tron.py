"""Tron, classic arcade game.

Exercises

1. Make the tron players faster/slower.
2. Stop a tron player from running into itself.
3. Allow the tron player to go around the edge of the screen.
4. How would you create a computer player?

"""

"""
Rule:-
1. we have blue & red snake and they are operated by different keys.
2. This is a multiplayer game, where the player try to avoid colliding anything.
"""

from turtle import *
from freegames import square, vector

p1xy = vector(-100, 0)  #first snake position
p1aim = vector(4, 0)  #setting the amount of pixel to move(4px horizontly right side)
p1body = set()  #taking an empty set which stores first snake body points

p2xy = vector(100, 0)  #second snake position
p2aim = vector(-4, 0)  #setting the amount of pixel to move(4px horizontly left side)
p2body = set()  #taking an empty set which stores second snake body points

def inside(head):
    """Return True if head inside screen."""
    return -200 < head.x < 200 and -200 < head.y < 200

def draw():
    "Advance players and draw game."
    p1xy.move(p1aim)  #moving the first snake by p1aim which we set earlier
    p1head = p1xy.copy()  #copying the x,y coordinates to p1head 

    p2xy.move(p2aim)  #moving the second snake by p2aim which we set earlier
    p2head = p2xy.copy()  #copying the x,y coordinates to p2head 

    if not inside(p1head) or p1head in p2body:  #if red snake touches the screen or blue snake then blue wins
        print('Player blue wins!')
        return

    if not inside(p2head) or p2head in p1body:  #if blue snake touches the screen or red snake then red wins
        print('Player red wins!')
        return

    p1body.add(p1head)  #storing p1head(which we copied) to p1body 
    p2body.add(p2head)  #storing p2head(which we copied) to p2body 

    square(p1xy.x, p1xy.y, 3, 'red')  #drawing body of first snake from all the stored coordinates, 3 is pensize
    square(p2xy.x, p2xy.y, 3, 'blue')  #drawing body of second snake from all the stored coordinates, 3 is pensize
    update()
    ontimer(draw, 50)  #drawing delay by 50ms

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()  #for listening the input from keyboard
onkey(lambda: p1aim.rotate(90), 'a')  #if we press 'a' then first snake will move left by 90 degree.
onkey(lambda: p1aim.rotate(-90), 'd')  #if we press 'd' then first snake will move right by 90 degree.
onkey(lambda: p2aim.rotate(90), 'j')  #if we press 'j' then second snake will move left by 90 degree.
onkey(lambda: p2aim.rotate(-90), 'l')  #if we press 'l' then second snake will move left by 90 degree.
draw()  #calling draw function that we made
done()
