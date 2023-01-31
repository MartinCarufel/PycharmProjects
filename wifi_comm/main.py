# Import socket module
import socket
from time import sleep

def ex1():

    # Create a socket object
    s = socket.socket()

    # Define the port on which you want to connect
    port = 12345
    ip_addr = '192.168.1.50'

    # connect to the server on local computer

    s.connect((ip_addr, port))
    # receive data from the server and decoding to get the string.
    # print(s.recv(1024).decode())
    sleep(1)
    msg = 'x'
    while msg.upper() != 'Q':

        msg = input("Entrer la commande:")
        s.send(msg.encode())
        # close the connection
    s.close()

def ex2():
    # Create a socket object
    s = socket.socket()

    # Define the port on which you want to connect
    port = 12345
    ip_addr = '192.168.1.50'

    # connect to the server on local computer

    s.connect((ip_addr, port))
    # receive data from the server and decoding to get the string.
    # print(s.recv(1024).decode())
    sleep(2)
    msg = input("activer le port 5, 6, 7 8, c for close: ")
    s.send(msg.encode())
    # input("Press enter")
    # s.send("5+".encode())
    # sleep(0.150)
    # s.send("5-".encode())

    # for i in range(100):
    #     s.send("5+".encode())
    #     sleep(0.095)
    #     s.send("5-".encode())
    #     sleep(0.095)
    s.close()

def ex3():
    # Create a socket object
    s = socket.socket()

    # Define the port on which you want to connect
    port = 12345
    ip_addr = '192.168.1.50'

    # connect to the server on local computer

    s.connect((ip_addr, port))
    # receive data from the server and decoding to get the string.
    # print(s.recv(1024).decode())
    sleep(2)
    msg = input("activer le port 5, 6, 7 8, c for close: ")
    s.send(msg.encode())
    # input("Press enter")
    # s.send("5+".encode())
    # sleep(0.150)
    # s.send("5-".encode())

    # for i in range(100):
    #     s.send("5+".encode())
    #     sleep(0.095)
    #     s.send("5-".encode())
    #     sleep(0.095)
    s.close()

ex1()

