import turtle
import random
import time
from turtle import Screen

wn = turtle.Screen()
wn.bgcolor("light blue")
turtle_instance = turtle.Turtle()
turtle_instance.turtlesize(5)
#Random atılacağı yer
b = 50
x, y = turtle.screensize()
x = int(x / 2)
y = int(y / 2)

#Counter
counter = turtle.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(0,turtle.screensize()[1]-5)
a = 20
score = 0
font = ("Arila",30,"normal")
def yazdir(x, y):
    global score
    print("tıklandı")
    score +=1

while a != 0:
    print(a)
    counter.write(f"Timer:{a} Score:{score}", font=font)
    counter.write("sa")
    time.sleep(1)
    a = a-1
    turtle_instance.penup()
    random_x = random.randint(-x, x)
    random_y = random.randint(-y, y)
    print(random_x, random_y)
    turtle_instance.goto(random_x, random_y)
    turtle_instance.onclick(yazdir)
    time.sleep(0.1)
    b -= 10
    counter.clear()
    if a==0:
        turtle_instance.hideturtle()
        counter.write(f"OYUN BİTTİ SKORUNUZ: {score}",font=font)
        break

turtle.done()