#!/usr/bin/env python 

""" 
A simple echo server 
"""
import sys
import socket

host = ''
port = 50000
backlog = 5
size = 1024
s = None
try:
    # http://ilab.cs.byu.edu/python/socket/exceptions.html
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(backlog)
except socket.error, (value, message):
    if s:
        s.close()
    print "Could not open socket: " + message
    sys.exit(1)
while 1:
    client, address = s.accept()
    data = client.recv(size)
    if data:
        client.send(data + "!!!")
    client.close()