import socket

HOST = '127.0.0.1'  # Localhost
PORT = 1234

def main():
    # Create a socket object
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Bind the socket to a specific address and port
        s.bind((HOST, PORT))
        # Listen for incoming connections
        s.listen()

        print(f"Listening on {HOST}:{PORT}")

        while True:
            # Wait for a connection
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                # Send a response to the client
                conn.sendall(b"Hello world!\n")

if __name__ == '__main__':
    main()
