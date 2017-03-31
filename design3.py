#imports turtle and function to create program
from myFunction import *
import turtle

bob=turtle.Turtle()
b=turtle.Turtle()
i=turtle.Turtle()
d=turtle.Turtle()
a=turtle.Turtle()
yi=turtle.Turtle()
f=turtle.Turtle()
t=turtle.Turtle()
e=turtle.Turtle()

#Making it so the the turtle can change color
turtle.colormode(255)

#Inceasing the speed of the turtle
a.speed(0)
e.speed(0)
i.speed(0)
d.speed(0)
bob.speed(0)
b.speed(0)
yi.speed(0)
f.speed(0)
t.speed(0)

#Changing the background color to black
turtle.bgcolor("black")

#Lists as variables 
sides=100
angle=5


#Color of the certain turtles
e.color("yellow")
f.color("green")
bob.color("yellow")
i.color("orange")
a.color("red")
yi.color("blue")

#Creates a circle made out of circles
for times in range(sides):
    i.circle(100)
    i.left(angle)
for times in range(sides):
    f.circle(200)
    f.left(angle)
    
#Creates a circle made out of triangles
for times in range(sides):
    polygon(a,3,1000)
    a.left(angle)
    
#Creates a circle made out of hexagons
for times in range(100):
    polygon(bob,6,50)
    bob.left(5)
    
#Creates a spiral out of squares
squarespiral(d)
b.goto(115,-40)

#Creates a spiral out of stars
starspiral(b)
t.left(165)
yi.left(105)

#Creates a three sided star
for times in range(85):
    c=(0,0,255-times)
    yi.color(c)
    print(c)
    polygon(yi,3,25)
    yi.left(120)
    yi.forward(times)
    
for times in range(85):
    c=(255-times,times,255-times)
    t.color(c)
    print(c)
    polygon(t,3,25)
    t.left(120)
    t.forward(times)
    
#Creates a circle inside the three sided star
for times in range(100):
    e.circle(5)
    e.left(5)

