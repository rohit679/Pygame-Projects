import turtle
import random
a=turtle.Turtle()
a.shape('turtle')
a.pensize(3)
b=turtle.Turtle()
b.shape('turtle')
b.pensize(3)
c=turtle.Turtle()
c.shape('turtle')
c.pensize(3)
d=turtle.Turtle()
d.shape('turtle')
d.pensize(3)
e=turtle.Turtle()
e.shape('turtle')
e.pensize(3)

a.color('red')
b.color('blue')
c.color('purple')
d.color('yellow')
e.color('green')

f=turtle.Turtle()
f.pensize(10)
f.penup()
f.setpos(-150,250)
f.pendown()
f.forward(300)
f.hideturtle()
x=-100
y=-250

a.penup()
a.setpos(x,y)
a.setheading(90)
a.pendown()

b.penup()
b.setpos(x+50,y)
b.setheading(90)
b.pendown()

c.penup()
c.setpos(x+100,y)
c.setheading(90)
c.pendown()

d.penup()
d.setpos(x+150,y)
d.setheading(90)
d.pendown()

e.penup()
e.setpos(x+200,y)
e.setheading(90)
e.pendown()

l=[1,2,3,4,5]
flag=1
while(flag):
    x=random.choice(l)
    if x==1:
        a.forward(5)
        if a.position()[1]>=250:
            print("red won")
            flag=0
    if x==2:
        b.forward(5)
        if b.position()[1]>=250:
            print("blue won")
            flag=0
    if x==3:
        c.forward(5)
        if c.position()[1]>=250:
            print("pink won")
            flag=0
    if x==4:
        d.forward(5)
        if d.position()[1]>=250:
            print("black won")
            flag=0
    if x==5:
        e.forward(5)
        if e.position()[1]>=250:
            print("green won")
            flag=0
    
    


