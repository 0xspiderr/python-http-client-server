#!/usr/bin/env python3
import socket

HOST: str = ''
PORT: int = 25000

# create server response and encode it
simple_response: str = "HTTP/1.1 200 OK\r\n" \
    "Content-Type: text/plain\r\n" \
    "Content-Length: 6 -- payload size\r\n" \
    "Connection: close\r\n\r\n" \
    "Hello!"
encoded_resp: bytes = simple_response.encode("ISO-8859-1")
# create socket and set options
sock = socket.socket()
# prevents 'address already in use' error when using bind in certain cases
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((HOST, PORT))
sock.listen()

while True:
    # await for a client request
    conn, addr = sock.accept()
    print("new connection from ", addr, "\n")
    # get connection request data
    while True:
        request = conn.recv(1024)
        decoded_req = request.decode("ISO-8859-1")
        print(decoded_req)
        if b"\r\n\r\n" in request:
            print("EOF data recv")
            break
    # send response
    conn.sendall(encoded_resp)
    # close the new connection
    conn.close()
