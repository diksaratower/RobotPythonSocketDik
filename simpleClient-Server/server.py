import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()

print('connected:', addr)

while True:
    kek = input("Введите сообщение: ")
    conn.send(kek.encode('utf-8'))

    data = conn.recv(1024)
    print(data.decode('utf-8'))

conn.close()
