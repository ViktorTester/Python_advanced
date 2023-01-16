import turtle as t

t.title("planets")
t.setup(1250, 480)
t.pensize(2)
t.hideturtle()
t.penup()
t.goto(-440, -50)
t.pendown()
t.speed('fast')

planets_size = [100, 20, 30, 18, 30, 60, 60, 40, 37, 10]
colors = ['#E3CF57', '#FFB90F', '#EEAD0E', '#7FFFD4', '#FF4040', '#FFB90F', '#CD9B1D',
          '#66CDAA', '#6495ED', '#FFC125']
planets_name = ['Sun', 'Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']


def saturn(side):
    t.seth(-45)
    for i in range(2):
        t.circle(side, 90)
        t.circle(side // 2, 90)
    t.seth(0)


for i in range(10):
    t.fillcolor(colors[i])
    t.begin_fill()
    t.circle(planets_size[i])
    t.end_fill()
    if planets_name[i] == 'Saturn':
        t.penup()
        t.goto(156, 20)
        t.pendown()
        saturn(85)
        t.penup()
        t.goto(216, -10)
    t.penup()
    t.right(90)
    t.forward(30)
    t.write(planets_name[i], move=False, align='center', font=('Times New Roman', 13, 'normal'))
    t.left(180)
    t.forward(30)
    if i == 9:
        break
    t.forward(planets_size[i])
    t.right(90)
    t.forward(planets_size[i] + planets_size[i + 1] + 30)
    t.right(90)
    t.forward(planets_size[i + 1])
    t.left(90)
    t.pendown()

t.exitonclick()

# The program draws the solar system.