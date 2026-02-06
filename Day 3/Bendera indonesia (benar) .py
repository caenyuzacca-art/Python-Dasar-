import turtle

t = turtle.Turtle()
t.speed(0)

def persegi_panjang(w, h, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(w)
        t.right(90)
        t.forward(h)
        t.right(90)
    t.end_fill()

# Merah (atas)
persegi_panjang(300, 100, "red")

# Putih (bawah)
t.right(90)
t.forward(100)
t.left(90)
persegi_panjang(300, 100, "white")

turtle.done()
