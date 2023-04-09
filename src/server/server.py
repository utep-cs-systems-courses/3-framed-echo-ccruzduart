#! /usr/bin/env python3
#
# server.py
#
# Made by: Cristian Cruz

import socket
import os
import time

# method sending the file content
def sendFile(conn, fileToSent):
    with open(fileToSent, 'rb') as f:
        while True:
            content = f.read(1000)
            if not content:
                break
            conn.send(content)

print("Server Starting...")

#setup server socket
host = 'localhost'
port = int(input("Enter port number:\n>> "))
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((host,port))
serverSocket.listen(1)
print(f"SetupL {host} : {port}")

# server will continuesly wait for clients
# once clients are connected it will sent requested files
while True:
    print("Server Ready...")
    conn,addr = serverSocket.accept()
    print(f"Client {addr} connected.")
    fileToSent = conn.recv(1024).decode()
    print(f"File requested: {fileToSent}")

    if os.path.isfile(fileToSent):
        conn.send(b"OK")
        time.sleep(0.5)
        sendFile(conn,fileToSent)
        print(f"File: {fileToSent} has been sent.")
    else:
        conn.send(b"ERROR")
        print(f"File {fileToSent} was not found")
