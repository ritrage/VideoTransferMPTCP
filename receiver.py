import socket
import tqdm
import os
import uu
import numpy as np
import cv2, time

SERVER_HOST = "0.0.0.0"

SERVER_PORT = 80

BUFFER_SIZE = 1048

MPTCP_ENABLED = 42

SEPARATOR = "<SEPARATOR>"

s = socket.socket()

s.setsockopt(socket.SOL_TCP,MPTCP_ENABLED,1)

#s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

s.bind((SERVER_HOST, SERVER_PORT))

s.listen(1)

print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

client_socket, address = s.accept()

print(f"[+] {address} is connected.")

received = client_socket.recv(BUFFER_SIZE).decode()

filename, filesize = received.split(SEPARATOR)

filename = os.path.basename(filename)

filesize = int(filesize)

with open(filename, "wb") as f:
    print("receiving")
    while True:
        bytes_read = client_socket.recv(BUFFER_SIZE)
        if not bytes_read:
            break
        f.write(bytes_read)
        print(bytes_read)
print("received")
client_socket.close()
s.close()

uu.decode(filename,"Video.mp4")

video  = cv2.VideoCapture("Video.mp4")

a=0
while True:
    a=a+1
    check, frame = video.read()
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow("Capturing", frame)
    
    key = cv2.waitKey(1)
    
    if(key==ord('q')):
        break

print(a)
video.release()
