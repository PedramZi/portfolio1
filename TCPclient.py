#!/usr/bin/env python

import socket

IP = '127.0.0.1'
port = 2022

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, port))

msg = s.recv(1024).decode('utf-8')
print(msg)

msgToSend = ""

while msgToSend != "Bye":

    msgToSend = input("Write something to server or 'Bye to end connection")

    encodedMsgToSend = msgToSend.encode('utf-8')

    s.send(encodedMsgToSend)

    msg_receive = s.recv(1024).decode('utf-8')

    print("Message from Server: " + msg_receive)

msg_receive = s.recv(1024).decode('utf-8')
print(msg_receive)


action_message = ""
def Thor(action_message):
    # action_message can be: "run", "jump", "swim"
    if action_message == "run":
        return "Would you like to run?".format(action_message + "ing").decode('utf-8')
    elif action_message == "train":
        return "how was your workout?".format(action_message + "ing").decode('utf-8')
    elif action_message == "swim":
        return "I cant swim".format(action_message + "ing").decode('utf-8')
    else:
        return "Im bored".format(action_message + "ing").decode('utf-8')



def Milen(action_message):
        if action_message == "run":
            return "Runnnn!!!".format(action_message + "ing").decode('utf-8')
        elif action_message == "workout":
            return "I do like to have workout everyday".format(action_message + "ing").decode('utf-8')
        elif action_message == "swim":
            return "who does not like to swiiiiim!!".format(action_message + "ing").decode('utf-8')
        else:
            return "Can we change the subject!".format(action_message + "ing").decode('utf-8')


reply = Thor(action_message)
reply = Milen(action_message)
print("Thor: {}".format(Thor(action_message)))
print("Milen: {}".format(Milen(action_message)))
action_message= s.send(action_message.encode('utf-8'))