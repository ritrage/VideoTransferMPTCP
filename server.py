import socket
import tqdm
import os
import uu

SERVER_HOST = "0.0.0.0"

SERVER_PORT = 8080

BUFFER_SIZE = 4096

MPTCP_ENABLED = 42

SEPARATOR = "<SEPARATOR>"

s = socket.socket()

s.setsockopt(socket.SOL_TCP,MPTCP_ENABLED,1)

s.bind((SERVER_HOST, SERVER_PORT))

s.listen(5)

print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")
client_socket, address = s.accept()

print(f"[+] {address} is connected.")

received = client_socket.recv(BUFFER_SIZE).decode()

filename, filesize = received.split(SEPARATOR)

filename = os.path.basename(filename)

filesize = int(filesize)

#progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scape=True, unit_divisor = 1024)
with open(filename, "wb") as f:
    while True:
        bytes_read = client_socket.recv(BUFFER_SIZE)
        if not bytes_read:
            break
        f.write(bytes_read)
        #progress.update(len(bytes_read))
        
client_socket.close()

s.close()

uu.decode(filename, "video.mp4")
