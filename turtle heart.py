import turtle 
wh = turtle.Screen()
wh.setup(width=400, height=400)
tur = turtle.Turtle()


def curva():
    for i in range(200):
        tur.right(1)
        tur.forwars(1)


def cuore():
    tur.fillcolor("red")
    tur.begin-fill()
    tur.left(140)
    tur.forward(113)
    curva()
    tur.left(120)
    curva()
    tur.forward(122)
    tur.end_fill()


cuore()
tur.ht()
turtle.done()
