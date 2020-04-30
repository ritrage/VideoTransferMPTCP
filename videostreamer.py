import socket
import tqdm
import os
import cv2, time
import uu

SEPARATOR = "<SEPARATOR>"

BUFFER_SIZE = 1048

host = "192.168.117.134"

port = 80

s = socket.socket()

print(f"[+] Connecting to {host}:{port}")

s.connect((host,port))

print("[+] Connected.")

uu.encode("video.mp4","video.txt")

filename = "video.txt"
filesize = os.path.getsize(filename)
s.send(f"{filename}{SEPARATOR}{filesize}".encode())
with open(filename, "rb") as f:
    print("sending...")
    while True:
        bytes_read = f.read(BUFFER_SIZE)
        if not bytes_read:
            break
        s.sendall(bytes_read)
print("sent")
s.close()

video= cv2.VideoCapture("video.mp4")

a=0

while True:
    a = a+1
    check, frame = video.read()
    
    print(check)
    print(frame)
    
    #gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Capturing", frame)
    
    key = cv2.waitKey(1)
    
    if key==ord('q'):
        break
    
print(a)
video.release()
