import socket

SERVER_IP = 'ENTER SERVER IP '
SERVER_PORT = 5678

def receive_file(conn):
    with conn:
        try:
            print("Receiving file from client...")
            with open('received_log.txt', 'wb') as file:
                while True:
                    data = conn.recv(2048)
                    if not data:
                        break
                    file.write(data)
            print("File received successfully.")
        except Exception as e:
            print(f"Error receiving file: {e}")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((SERVER_IP, SERVER_PORT))
    print('Server listening...')
    s.listen(1)
    conn, addr = s.accept()
    print(f'Connected to {addr}')

    # Recebe o arquivo do cliente
    receive_file(conn)
