import turtle as t
import random as r

t.title("buildings")
t.hideturtle()
t.bgcolor('navy')
t.setup(700, 650)
t.speed('fastest')


def stars(count):
    for i in range(count):
        pos_x = r.randint(-330.00, 330.00)
        pos_y = r.randint(-150.00, 300.00)
        t.penup()
        t.goto(pos_x, pos_y)
        t.pendown()
        t.pencolor('yellow')
        t.fillcolor('yellow')
        t.begin_fill()
        t.circle(r.randint(1, 4))
        t.end_fill()


def buildings(count, counter=0):
    for j in range(count):
        t.pencolor('midnight blue')
        t.fillcolor('midnight blue')
        t.begin_fill()
        x = 120
        y = [200, 350, 550, 310, 500, 200]
        for i in range(2):
            t.forward(x)
            t.left(90)
            t.forward(y[counter])
            t.left(90)
        t.end_fill()
        counter += 1
        t.forward(x)


def windows(count, counter=0):
    for m in range(count):
        windows_list = [[-330, -190], [-290, -190], [-210, -35], [-170, -35],
                        [-130, -95], [-25, 170], [25, -70], [100, -130], [145, 60], [215, 115]]
        t.pencolor('gold')
        t.fillcolor('gold')
        t.penup()
        t.goto(windows_list[counter])
        t.pendown()
        t.begin_fill()
        for h in range(2):
            t.forward(20)
            t.left(90)
            t.forward(40)
            t.left(90)
        t.end_fill()
        counter += 1


stars(100)

t.penup()
t.goto(-350, -325)
t.pendown()

t.speed('fast')

buildings(6)

t.speed('slow')

windows(10)

# The program draws silhouettes of buildings against the starry sky.