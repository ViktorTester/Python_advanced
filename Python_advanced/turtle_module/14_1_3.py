import turtle as t


def triangle(side):
    t.shape('turtle')
    for _ in range(3):
        t.forward(side)
        t.left(120)

triangle(123)

# The program draws a regular triangle using turtle module.