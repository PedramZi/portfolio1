#!/usr/bin/env python

import socket

"""The first argument AF_INET is the address domain of the
socket. This is used when we have an Internet Domain with
any two hosts The second argument is the type of socket.
SOCK_STREAM means that data or characters are read in
a continuous flow."""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

"""
binds the server to an entered IP address and at the
specified port number.
The client must be aware of these parameters
"""
s.bind(('127.0.0.1', 2022))

"""
listens for 5 active connections. This number can be
increased as per convenience.
"""
s.listen(5)

#Using the below function, we broadcast the message to all
#clients who's object is not the same as the one sending
#the message

#removed

#The following function simply removes the object
#from the list that was created at the beginning of
#the program

#removed


"""
accept qotd_client
send msg to client
accept msg from client
kick function
"""


while True:

    print("Waiting for connection... (Please wait!)")
    data, source = s.accept()

    print("Connect with", source, "established")

    msg_send = "Hello, You are connected to the server!".encode('utf-8')
    data.send(msg_send)

    while True:
        some_msg = data.recv(1024).decode('utf-8')
        print("Msg from Client:" + some_msg)

        if some_msg == "Bye":
            break

        response_msg = input("write something to Client: ")
        msg_send = response_msg.encode('utf-8')
        data.send(msg_send)
        print("Client is typing ...")

    msg_send = "Bye received, connection ended.".encode('ytf-8')
    data.send(msg_send)
    data.close()
    break
