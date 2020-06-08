import turtle
import random

a=turtle.Turtle()  #for creating first pointer
a.shape('turtle')
a.pensize(3)
a.color('red')

b=turtle.Turtle()  #for creating second pointer
b.shape('turtle')
b.pensize(3)
b.color('blue')

c=turtle.Turtle()  #for creating third pointer
c.shape('turtle')
c.pensize(3)
c.color('purple')

d=turtle.Turtle()  #for creating fourth pointer
d.shape('turtle')
d.pensize(3)
d.color('yellow')

e=turtle.Turtle()  #for creating fifth pointer
e.shape('turtle')
e.pensize(3)
e.color('green')


f=turtle.Turtle()  #for creating other pointer for creating border and finishing line
f.pensize(8)
f.penup()
f.setpos(-200,300)
f.pendown()
f.forward(400)
f.right(90)
f.forward(600)
f.right(90)
f.forward(400)
f.right(90)
f.forward(600)
f.right(90)
f.penup()
f.setpos(-150,250)
f.pendown()
f.forward(300)
f.hideturtle()  #So till now border and finishing line is being created

x=-100  #setting the initial coordinate of the first racing turtle
y=-250

a.penup()  #moving first turtle to the initial position
a.setpos(x,y)
a.setheading(90)
a.pendown()

b.penup()  #moving second turtle to the initial position
b.setpos(x+50,y)
b.setheading(90)
b.pendown()

c.penup()  #moving third turtle to the initial position
c.setpos(x+100,y)
c.setheading(90)
c.pendown()

d.penup()  #moving fourth turtle to the initial position
d.setpos(x+150,y)
d.setheading(90)
d.pendown()

e.penup()  #moving fifth turtle to the initial position
e.setpos(x+200,y)
e.setheading(90)
e.pendown()

l=[1,2,3,4,5]  #list variable which is having ids of all the turtle
flag=1  #  for terminating condition
speed=2.5  #setting the speed
while(flag):  #run until the flag variable gets 0
    x=random.choice(l)  #choose any value randomly from l
    if x==1:  #if it's 1 then move first turtle by speed
        a.forward(speed)
        if a.position()[1]>=250:  #checking if the turtle crossing the finishing line
            print("red won")
            flag=0
    if x==2:  #doing same for rest of the turtle
        b.forward(speed)
        if b.position()[1]>=250:
            print("blue won")
            flag=0
    if x==3:
        c.forward(speed)
        if c.position()[1]>=250:
            print("pink won")
            flag=0
    if x==4:
        d.forward(speed)
        if d.position()[1]>=250:
            print("black won")
            flag=0
    if x==5:
        e.forward(speed)
        if e.position()[1]>=250:
            print("green won")
            flag=0
    
    


