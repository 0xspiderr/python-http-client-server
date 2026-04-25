#!/usr/bin/env python3

import socket

sock = socket.socket()
http_req: str = "GET / HTTP/1.1 \
Host: example.com \
Connection: close"
encoded_req: bytes = http_req.encode("ISO-8859-1")
sock.connect(("example.com", 80))
sock.sendall(encoded_req)

response = sock.recv(4096)
decoded_response = response.decode("ISO-8859-1")
print(decoded_response)
if len(response) == 0:
    print("done")

sock.close()
