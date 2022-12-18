import turtle as t

def rectangle(width, height):
    t.shape('turtle')
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)

rectangle(200, 100)

# The program draws a rectangle using turtle module.