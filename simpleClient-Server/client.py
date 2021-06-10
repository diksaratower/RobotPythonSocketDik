import socket

sock = socket.socket()
sock.connect(('localhost', 9090))


while True:
    kek = input("Введите сообщение: ")
    sock.send(kek.encode('utf-8'))

    data = sock.recv(1024)
    print(data.decode('utf-8'))