#For GUI
from turtle import Turtle, Screen
#For Communication.
from socket import socket, AF_INET, SOCK_STREAM
#For Multi-threading.
from _thread import start_new_thread
#For delay
from time import sleep
import random
import turtle


def send_function(x):
    keypress = str(x) 
    #print(keypress)
    s.send(keypress.encode('UTF-8'))

def gameloop(s):
    # Main game loop
    while True:
        wind.update()
        
def up():
    figure.forward(10)
    x = 'w'
    send_function(x)

def left():
    figure.left(45)
    x = 'a'
    send_function(x)

def right():
    figure.right(45)
    x = 'd'
    send_function(x)

def down():
    figure.backward(10)
    x = 's'
    send_function(x)

def increase():
    figure.shapesize(5,5)
    x='Up'
    send_function(x)

def decrease():
	figure.shapesize(2,2)
	x='Down'
	send_function(x)

def color():
  	figure.color('blue')
  	x='Left'
  	send_function(x)

def color2():
  	figure.color('red')
  	x='Right'
  	send_function(x)

def bye():
	x = 'Escape'
	send_function(x)
	wind.bye()

wind = Screen()
wind.title("TURTLE: Client Side")
wind.bgcolor("#222222")
wind.setup(width=1024, height=768)
wind.tracer(0)


figure = Turtle()
figure.speed(0)
figure.shape("turtle")
figure.shapesize(2,2)
figure.color("red")
figure.penup()
figure.goto(0, 0)

text = ''

# Keyboard binding
wind.listen()
wind.onkeypress(up, "w")
wind.onkeypress(down, "s")
wind.onkeypress(right, "d")
wind.onkeypress(left, "a")
wind.onkeypress(increase, "Up")
wind.onkeypress(color, "Left")
wind.onkeypress(color2, "Right")
wind.onkeypress(decrease, "Down")
wind.onkeypress(bye, "Escape")

s=socket(AF_INET, SOCK_STREAM)
s.connect(('192.168.0.104',7010))
#create thread for serving that session.

start_new_thread(gameloop,(s,))
wind.mainloop()
