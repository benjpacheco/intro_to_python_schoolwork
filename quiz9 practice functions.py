import turtle
tess turtle.Turtle()
tess.shape('Turtle')

def ramble(t, len):
    if len <= 10:
        t.stamp()
    elif len%2 == 0:
        t.left(90)
        t.forward(len)
        ramble(t, len//2)
    else:
        t.right(90)
        t.forward(len)
        ramble(t, len//2)
