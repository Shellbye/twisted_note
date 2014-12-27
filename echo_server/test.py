__author__ = 'shellbye'
import socket


def test(port=1234, host="localhost", receive_max_size=1024):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.send("Hello, World!")
    data = s.recv(receive_max_size)
    s.close()
    print "Echo from echo_server:", data

if __name__ == "__main__":
    print "i am test"
    # test()
    test(50000)