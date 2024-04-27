import socket

# Define the host and port to listen on
port = 0
host = ''


# Create a socket object
def create_socket():
    try:
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Bind the socket to the server address
        sock.bind((host, port))
        # Listen for incoming connections
        sock.listen(1)
        print(f"Packet logger listening on {host}:{port}")
        return sock
    except socket.error as e:
        print(f"Error creating socket: {e}")
        return None


# Log packets received from the socket
def logger(sock):
    try:
        while True:
            # Wait for a connection
            connection, client_address = sock.accept()
            try:
                print(f"Connection from {client_address}")

                # Receive data in small chunks and log
                while True:
                    data = connection.recv(1024)
                    if data:
                        print(f"Received: {data}")
                    else:
                        break

            finally:
                # Clean up the connection
                connection.close()

    except KeyboardInterrupt:
        print("Packet logger stopped.")

if __name__ == "__main__":
    sock = create_socket()
    if sock:
        logger(sock)
