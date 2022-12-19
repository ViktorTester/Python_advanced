import turtle as t

t.shape('turtle')
t.speed('slowest')
def square(side):
    for _ in range(4):
        t.forward(side)
        t.left(90)


for _ in range(8):
    t.left(45)
    square(120)

# The program draws a figure of eight squares using turtle module.