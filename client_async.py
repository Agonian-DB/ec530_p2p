import socket
import threading

def listen_for_messages(client_socket):
    """Thread function to constantly listen for messages from the server."""
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"\n[Server]: {data.decode()}")
        except:
            break

def main():
    host = '127.0.0.1'
    port = 65432

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print("Connected to the server.")

    # Start a thread to listen for incoming messages
    listener = threading.Thread(target=listen_for_messages, args=(client_socket,), daemon=True)
    listener.start()

    print("Type your message and press Enter. Type 'exit' to quit.")
    while True:
        message = input(">> ")
        if message.lower() == 'exit':
            break
        client_socket.sendall(message.encode())

    client_socket.close()

if __name__ == '__main__':
    main()