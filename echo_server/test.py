__author__ = 'shellbye'
import socket
from echo_server0 import HOST, PORT

RECEIVE_SIZE = 1024


def test_echo0():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.send("Hello, World!\r\t")
    data = s.recv(1024)
    s.close()
    print "Echo from echo_server0:", data


def test_echo():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, 1234))
    s.send("Hello, World!")
    data = s.recv(RECEIVE_SIZE)
    s.close()
    print "Echo from echo_server:", data


if __name__ == "__main__":
    print "i am test"
    test_echo()