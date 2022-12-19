import turtle as t


def square(side):
    t.shape('turtle')
    t.speed('slowest')
    for i in range(3):
        t.left(20)
        for j in range(4):
            t.forward(side)
            t.left(90)

square(100)

# The program draws three squares, offset from each other by 30 degrees using turtle module.