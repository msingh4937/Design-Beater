import turtle
import random
turtle.colormode(255)#brings in the colormode function
turtle.bgcolor('black')
bob = turtle.Turtle()
tom = turtle.Turtle()
from myFunctionfile import*
bob.pensize(4)
tom.pensize(5)
bob.speed(0)
tom.speed(0)

for n in range(160):
    c = (n,237,255)
    bob.color(c)
    bob.circle(n)
    bob.right(10000)
    bob.circle(500)

jump(tom,0,0)
tom.penup()
tom.goto(-325,335)
tom.pendown()


tom.color('white')
polygonf(tom,4,700)



jump(bob,0,0)
bob.penup()
bob.goto(-325,335)
bob.pendown()

for n in range (100):
    bob.color('red')
    angle = random.randint(0,45)
    bob.right(angle)
    distance = random.randint(0,150)
    bob.forward(distance)
    bob.backward(distance)

    
    

  
                
turtle.done()
