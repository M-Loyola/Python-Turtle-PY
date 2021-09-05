#For GUI
from turtle import Turtle, Screen
#For Communication.
from socket import socket, AF_INET, SOCK_STREAM
#For Multi-threading.
from _thread import start_new_thread
#For delay
from time import sleep
import turtle


def receive_thread(c):
    while True:
        x = c.recv(500).decode('UTF-8')
        if x == 'w':
        	figure.forward(10)
        elif x =='d':
        	figure.right(45)
        elif x == 'a':
        	figure.left(45)
        elif x == 's':
        	figure.backward(10)
        elif x == 'Left':
        	figure.color('blue')
        elif x == 'Right':
        	figure.color('red')
        elif x == 'Up':
        	figure.shapesize(5,5)
        elif x == 'Down':
        	figure.shapesize(2,2)
        else:
        	wind.bye()


def gameloop(c):
    # Main game loop
    while True:
        wind.update()
        
 
wind = Screen()
wind.title("TURTLE: Server Side")
wind.bgcolor("#222222")
wind.setup(width=1024, height=768)
wind.tracer(0)


# Paddle B
figure = Turtle()
figure.speed(0)
figure.shape("turtle")
figure.shapesize(2,2)
figure.color("red")
figure.penup()
figure.goto(0, 0)

#Creating an unbounded socket.
s=socket(AF_INET, SOCK_STREAM)
#Defining the server's IP.
host = '192.168.0.104'
#Defining the server's port number of the service.
port = 7010
#Binding both IP and port number to each other.
s.bind((host, port))
#Waiting for a client to connect.
s.listen(1)
print ("Server established")

#Accept a request for connection from a client,
#return both session number, and information about the connected client (IP and port number)
c, add=s.accept()
print ("connection established")
#create thread for serving that session.
start_new_thread(receive_thread,(c,))

start_new_thread(gameloop,(c,))
wind.mainloop()
