# Socket programming example: client side config.
# Import the socket module to work with network sockets
import socket

# Define a function for the client side of the socket example
def socket_example_client():
    # Define the server's host and port the client will connect to
    host = '127.0.0.1'
    port = 65525

    # Create a socket using IPv4 and TCP protocol
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Connect to the destination host and port
        s.connect((host, port))

        # Send a request message to the server
        s.sendall(b'Hello Server, I am the client.')

        # Capture the response from the server (up to 1024 bytes)
        data = s.recv(1024)

    # Print the received data from the server
    print('Received the data!', repr(data))

