import turtle
from random import *
turtle.colormode(255)

def quadrado(tamanho):
    c = 0
    while c < 5:
        turtle.forward(tamanho)
        turtle.right(90)
        turtle.forward(tamanho)
        turtle.right(90)
        turtle.forward(tamanho)
        turtle.right(90)
        turtle.forward(tamanho)
        c += 1
        tamanho += 50
        turtle.speed(10)
        

seq = 0

while seq < 15:
    print(quadrado(50))
    seq += 1
