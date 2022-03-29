import socket
import sys
import errno

HEADER_LENGTH = 10

IP = "127.0.0.1"
PORT = 1234
my_username = input("Username: ")

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to a given ip and port
client_socket.connect((IP, PORT))

# Set connection to non-blocking state, so .recv() call won;t block, just return some exception we'll handle
client_socket.setblocking(False)

# Prepare username and header and send them
username = my_username.encode('utf-8')
username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
client_socket.send(username_header + username)

while True:

    # username's input
    message = input(f'{my_username} > ')

    # If message is not empty - send it
    if message:

        # Encode message to bytes, prepare header and convert to bytes, like for username above, then send
        message = message.encode('utf-8')
        message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
        client_socket.send(message_header + message)


    try:
        # Now we want to loop over received messages (there might be more than one) and print them
        while True:

            # Receive our "header" containing username length, it's size is defined and constant
            username_header = client_socket.recv(HEADER_LENGTH)

            # If we received no data, server gracefully closed a connection
            if not len(username_header):
                print('Connection closed by the server')
                sys.exit()

            # Convert header to int value
            username_length = int(username_header.decode('utf-8').strip())

            # Receive and decode username
            username = client_socket.recv(username_length).decode('utf-8')

            # Now do the same for message (as we received username, we received whole message)
            message_header = client_socket.recv(HEADER_LENGTH)
            message_length = int(message_header.decode('utf-8').strip())
            message = client_socket.recv(message_length).decode('utf-8')

            if message == action_message:
                def Thor(action_msg):
                    # action_message can be: "run", "jump", "swim"
                    if action_msg == "run":
                        return "Would you like to run?".format(action_msg + "ing")
                    elif action_msg == "train":
                        return "how was your workout?".format(action_msg + "ing")
                    elif action_msg == "swim":
                        return "I cant swim".format(action_msg + "ing")
                    else:
                        return "Im bored".format(action_msg + "ing")


                def Milen(action_msg):
                    if action_msg == "run":
                        return "Runnnn!!!".format(action_msg + "ing")
                    elif action_msg == "workout":
                        return "I do like to have workout everyday".format(action_msg + "ing")
                    elif action_msg == "swim":
                        return "who does not like to swiiiiim!!".format(action_msg + "ing")
                    else:
                        return "Can we change the subject!".format(action_msg + "ing")

                action_msg = action_message

                reply = Thor(action_msg)
                reply = Milen(action_msg)
                action_message = client_socket.send(action_message.encode('utf-8'))

            # Print message
            print(f'{username} > {message}')
            print("Thor: {}".format(Thor(action_msg)))
            print("Milen: {}".format(Milen(action_msg)))
            action_message = client_socket.send(action_message.encode('utf-8'))

    except IOError as e:
        # This is normal on non blocking connections - when there are no incoming data error is going to be raised
        # Some operating systems will indicate that using AGAIN, and some using WOULDBLOCK error code
        # We are going to check for both - if one of them - that's expected, means no incoming data, continue as normal
        # If we got different error code - something happened
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Reading error: {}'.format(str(e)))
            sys.exit()

        # We just did not receive anything
        continue

    except Exception as e:
        # Any other exception - something happened, exit
        print('Reading error: '.format(str(e)))
        sys.exit()
