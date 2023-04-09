#! /usr/bin/env python3
#
# client.py
#
# made by: Cristian Cruz

import os
import socket

#method that receives the content from the server and copying them
def receiveFile(conn,fileReceive):
    with open(fileReceive, 'wb') as f:
        while True:
            conn.settimeout(1)
            try:
                content = conn.recv(1000)
                if content is None or content == "":
                    break
                f.write(content)
            except socket.timeout:
                break

print("Starting client...")

#setup connection to server
print("Please enter the following server information")
host = input("Enter the server IP address:\n>> ")
port = int(input("Enter server port nnumber:\n>> "))

#Creating client socket and connecting to server socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((host,port))
print(f"Connected to server {host} : {port}")

#start transfer process
fileReceive = input("Enter the file name to be receive:\n>> ")
clientSocket.sendall(fileReceive.encode())
response = clientSocket.recv(1024)
if response == b"OK":
    receiveFile(clientSocket, fileReceive)
    print(f"File {fileReceive} received.")
elif response == b"ERROR":
    print(f"Error, File {fileReceive} was not found.")
print("Client closing...")
clientSocket.close()
