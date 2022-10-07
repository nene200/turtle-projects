from turtle import *

tom = Turtle()

tom.pensize(10)
tom.penup()
tom.goto(-200, 0)
tom.pendown()

# The letter N
tom.left(90)
tom.forward(80)
tom.right(140)
tom.forward(100)
tom.left(140)
tom.forward(80)

tom.penup()
tom.goto(-100, 0)
tom.pendown()

# The letter E
tom.forward(80)
tom.right(90)
tom.forward(50)
tom.backward(50)
tom.right(90)
tom.forward(40)
tom.left(90)
tom.forward(50)
tom.backward(50)
tom.right(90)
tom.forward(40)
tom.left(90)
tom.forward(50)

tom.penup()
tom.goto(0, 0)
tom.pendown()

# The letter N
tom.left(90)
tom.forward(80)
tom.right(140)
tom.forward(100)
tom.left(140)
tom.forward(80)

tom.penup()
tom.goto(100, 0)
tom.pendown()

tom.forward(80)
tom.right(90)
tom.forward(50)
tom.backward(50)
tom.right(90)
tom.forward(40)
tom.left(90)
tom.forward(50)
tom.backward(50)
tom.right(90)
tom.forward(40)
tom.left(90)
tom.forward(50)

done()