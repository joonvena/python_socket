#!/usr/bin/env python3

import socket
import random

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

def random_data():
    y = random.randint(1,1000)
    x = random.randint(1,1000)
    my_data = "{},{}".format(x,y)
    return my_data

def my_server():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(5)
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            my_data = random_data()
            encoded_data = my_data.encode('utf-8')
            conn.sendall(encoded_data)


if __name__ == '__main__':
    while 1:
        my_server()