from turtle import *


pen = Turtle()

pen.pensize(10)
pen.penup()
pen.goto(-300,0)
pen.pendown()

pen.left(90)
pen.forward(100)
pen.right(146)
pen.forward(120)
pen.left(146)
pen.forward(100)

pen.penup()
pen.goto(-200,0)
pen.pendown()

pen.forward(100)
pen.right(146)
pen.forward(120)
pen.left(146)
pen.forward(100)

pen.penup()
pen.goto(-100,0)
pen.pendown()

pen.forward(100)
pen.right(90)
pen.forward(60)
pen.backward(60)
pen.right(90)
pen.forward(50)
pen.left(90)
pen.forward(60)
pen.backward(60)
pen.right(90)
pen.forward(50)
pen.left(90)
pen.forward(60)

pen.penup()
pen.goto(50,0)
pen.pendown()

for degree in range(30):
    pen.left(degree)
    pen.forward(degree)

pen.penup()
pen.goto(140,0)
pen.pendown()
pen.left(15)

pen.forward(100)
pen.right(146)
pen.forward(60)

pen.penup()
pen.goto(212,0)
pen.pendown()

pen.right(214)

pen.forward(100)
pen.left(146)
pen.forward(60)

pen.penup()
pen.goto(250, 0)
pen.pendown()

pen.left(200)
pen.forward(100)
pen.right(150)
pen.forward(100)
pen.backward(50)
pen.right(100)
pen.forward(20)

done()