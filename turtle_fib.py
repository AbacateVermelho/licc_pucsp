import turtle
from random import *
turtle.colormode(255)
turtle.up()
turtle.goto(-300, -200)
turtle.down()

def cor():
    r = randrange(0, 255)
    g = randrange(0, 255)
    b = randrange(0, 255)
    return(r, g, b)

def quadrado(tamanho):
    turtle.begin_fill()
    turtle.fillcolor(cor())
    turtle.forward(tamanho)
    turtle.left(90)
    turtle.forward(tamanho)
    turtle.left(90)
    turtle.forward(tamanho)
    turtle.left(90)
    turtle.forward(tamanho)
    turtle.left(90)
    turtle.forward(tamanho)
    turtle.speed(100)
    turtle.end_fill()

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


for i in range(50):
    print(quadrado(fib(i)))

        
