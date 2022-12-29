import turtle

turtle.shape('turtle')
turtle.speed('slow')
turtle.color("red", "black")
turtle.bgcolor("lightgreen")
turtle.pensize(8)

turtle.goto(200, 0)
turtle.goto(100, 100)
turtle.goto(0, 0)
turtle.penup()
turtle.goto(0, 60)
turtle.pendown()
turtle.goto(200, 60)
turtle.goto(100, -50)
turtle.goto(0, 60)


turtle.exitonclick()

# The program draws a star