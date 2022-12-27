import turtle

def star(side):
    turtle.shape('turtle')
    turtle.color("blue", "green")
    turtle.pensize(5)
    for _ in range(2):
        turtle.penup()
        turtle.forward(side)
        turtle.stamp()
        turtle.left(180)
        turtle.forward(side)



def count(side):
    for _ in range(5):
        star(side)
        turtle.left(360 / 10)

count(121)
turtle.shape('turtle')
turtle.left(180)
turtle.stamp()
turtle.exitonclick()

# The program displays a star with turtles at the ends of the rays, without lines.