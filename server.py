import socket
import random
import json

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print('Starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

def random_data():
    y = random.randint(1,1000)
    x = random.randint(1,1000)
    my_data = {'coordY': 'test', 'coordX': 'test'}
    return my_data

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(1024)
            print('received {!r}'.format(data))
            if data:
                my_data = random_data()
                to_json = json.dumps(my_data).encode('utf-8')
                print('sending data back to the client')
                connection.sendall(to_json)
            else:
                print('no data from', client_address)
                break

    finally:
        # Clean up the connection
        print("Closing current connection")
        connection.close()