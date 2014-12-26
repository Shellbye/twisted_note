__author__ = 'shellbye'
import socket


def test_echo():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("localhost", 1234))
    s.send("Hello, World!")
    data = s.recv(1024)
    s.close()
    print "Echo from echo_server:", data


def test_echoserver_simple():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("localhost", 50000))
    s.send("Hello, World!")
    data = s.recv(1024)
    s.close()
    print "Echo from echo_server:", data

if __name__ == "__main__":
    print "i am test"
    # test_echo()
    test_echoserver_simple()