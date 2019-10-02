#!/usr/bin/env python3

import socket
import time

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server
LIMIT = 0

def process_data_from_server(x):
    x1, y1 = x.split(",")
    return x1,y1

def my_client():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        data = s.recv(1024).decode('utf-8')
        x_val,y_val = process_data_from_server(data)
        print("Y-coord {}".format(x_val))
        print("X-coord{}".format(y_val))
        s.close()
        time.sleep(5)
    

if __name__ == "__main__":
    while 1:
        my_client()