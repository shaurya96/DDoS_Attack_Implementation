# Import the socket module to work with network sockets
import socket

# Define a function for the server side of the socket example
def socket_example_server():
    # Define the host and port the server will listen on
    host = '127.0.0.1'
    port = 65525

    # Create a socket using IPv4 and TCP protocol
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Associate the host and port with the socket
        s.bind((host, port))

        # Start listening for incoming connections
        s.listen()

        # Accept an incoming connection and get the connection object (conn) and client address (addr)
        conn, addr = s.accept()

        # Process the request and reply to the client
        with conn:
            print('Connected by', addr)
            while True:
                # Receive data from the client (up to 1024 bytes at a time)
                data = conn.recv(1024)
                if not data:
                    # If no data is received, exit the loop
                    break
                # Send a response to the client, acknowledging receipt of their data
                conn.sendall(b"Hello Client, the server has received your data!")
                print(data)  # Print the received data (you may want to process it)

