import turtle

t = turtle.Turtle()
t.speed(0)
t.color("red", "pink")

t.begin_fill()
for i in range(36):
    t.circle(100)
    t.left(10)
t.end_fill()

turtle.done()
