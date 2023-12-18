# Import the socket and sys modules
import socket
import sys

# Define a function for the server side of the socket example
def socket_example_server():
    try:
        # Create a socket using IPv4 and TCP protocol
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Define the server's IP address and port
        server_address = ('127.0.0.1', 65525)
        
        # Bind the server socket to the specified address
        server_socket.bind(server_address)
        print("\nServer Socket Successfully Created\n")
        
        # Listen for incoming client connections
        server_socket.listen()
        print("\nWaiting for Client Connection\n")
        
        while True:
            try:
                # Accept a client connection and get the client socket and client address
                client_socket, client_address = server_socket.accept()
                print("\nConnection established with\t", client_address)
                
            except Exception as e:
                print(e)
                server_socket.close()
                sys.exit(0)
    except Exception as e:
        print("\nFailure in Server socket creation\nError:", e, "\n")
        sys.exit(0)

# Define a main function to run the server example
def main():
    socket_example_server()

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
	

                
