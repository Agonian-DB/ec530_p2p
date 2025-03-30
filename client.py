import socket

def main():
    host = '127.0.0.1'  # Server IP address
    port = 65432        # Server port (must match the server's port)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print("Connected to the server. Type your message and press Enter. Type 'exit' to quit.")

    while True:
        message = input(">> ")
        if message.lower() == 'exit':
            break

        client_socket.sendall(message.encode())
        data = client_socket.recv(1024)
        print(f"Server replied: {data.decode()}")

    client_socket.close()

if __name__ == '__main__':
    main()