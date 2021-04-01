
import socket
import time
import keyboard

server = socket. socket(

   socket. AF_INET,
   socket. SOCK_STREAM,
   
   )
   
server. bind(
 ("192.168.1.67", 1234) # localhost
 )
 
server. listen(5)

while True:
    user_socket, address = server. accept()
    print(f"Подключено к {address}")
    break

time.sleep(1)

#user_socket.send(bytes("Это точно", "utf-8"))
def stop():
	user_socket.send("stop".encode("utf-8"))

def right():
	user_socket.send("right".encode("utf-8"))

def left():
	user_socket.send("left".encode("utf-8"))

def back():
	user_socket.send("back".encode("utf-8"))

def forward():
	user_socket.send("forward".encode("utf-8"))

keyboard.add_hotkey('0', stop)



keyboard.add_hotkey('d', right)
keyboard.add_hotkey('a', left)
keyboard.add_hotkey('w', forward)
keyboard.add_hotkey('s', back)


keyboard.wait('Ctrl + Q')


 
