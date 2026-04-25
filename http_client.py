#!/usr/bin/env python3

import socket

# prepare socket obj and request http header
sock = socket.socket()
# must send double carriage return linefeeds at the end
# for the server to know that the transmission is over
http_req: str = "GET / HTTP/1.1\r\n" \
                "Host: example.com\r\n" \
                "Connection: close\r\n\r\n"
# ISO-8859-1 is the standard encoding for the web
encoded_req: bytes = http_req.encode("ISO-8859-1")

# socket connection and send data
sock.connect(("example.com", 80))
sock.sendall(encoded_req)

# wait for http response
while True:
    # get at most 1024 bytes, loop until we get no more bytes
    response = sock.recv(1024)
    decoded_response = response.decode("ISO-8859-1")
    print(decoded_response)
    if len(response) == 0:
        print("EOF transmission")
        break

# close conn
sock.close()
