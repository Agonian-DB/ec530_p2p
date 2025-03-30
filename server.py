import socket
import threading

def handle_client(conn, addr):
    print(f"Connected from {addr}")
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break  # Client disconnected
            print(f"Received from {addr}: {data.decode()}")
            # Echo the message back to the client
            conn.sendall(data)
        except Exception as e:
            print(f"Error: {e}")
            break
    conn.close()
    print(f"{addr} disconnected")

def main():
    host = '127.0.0.1'  # Local address
    port = 65432        # Port number (customize if needed)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()
    print(f"Server started, listening on {host}:{port}")

    while True:
        conn, addr = server_socket.accept()
        # Create a new thread for each client
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == '__main__':
    main()