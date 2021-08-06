import pyfirmata
import time
import keyboard
import socket

board = pyfirmata.Arduino('com3')
#board = pyfirmata.Arduino('/dev/ttyUSB0')


gaz = 1

left_forw = board.get_pin('d:3:p')
left_back = board.get_pin('d:5:p')

right_forw = board.get_pin('d:6:p')
right_back = board.get_pin('d:11:p')

ruka_clouse = board.get_pin('d:12:o')
ruka_open = board.get_pin('d:8:o')

ruka_up = board.get_pin('d:10:p')
ruka_down = board.get_pin('d:9:p')


def stop():
    left_forw.write(0)
    left_back.write(0)
    right_forw.write(0)
    right_back.write(0)
    ruka_open.write(0)
    ruka_clouse.write(0)
    ruka_up.write(0)
    ruka_down.write(0)


def right():
    left_forw.write(gaz)
    left_back.write(0)
    right_forw.write(0)
    right_back.write(gaz)


def left():
    left_forw.write(0)
    left_back.write(gaz)
    right_forw.write(gaz)
    right_back.write(0)


def back():
    left_forw.write(0)
    left_back.write(gaz)
    right_forw.write(0)
    right_back.write(gaz)


def forward():
    left_forw.write(gaz)
    left_back.write(0)
    right_forw.write(gaz)
    right_back.write(0)


def fun_ruka_open():
    ruka_open.write(0)
    ruka_clouse.write(1)


def fun_ruka_clouse():
    ruka_open.write(1)
    ruka_clouse.write(0)


def fun_ruka_up():
    ruka_up.write(1)
    ruka_clouse.write(0)


def fun_ruka_down():
    ruka_up.write(0)
    ruka_down.write(0.3)


while True:
    if keyboard.is_pressed('d'):
        right()
    if keyboard.is_pressed('a'):
        left()
    if keyboard.is_pressed('w'):
        forward()
    if keyboard.is_pressed('s'):
        back()
    if keyboard.is_pressed('t'):
        fun_ruka_open()
    if keyboard.is_pressed('g'):
        fun_ruka_clouse()
    if keyboard.is_pressed('f'):
        fun_ruka_up()
    if keyboard.is_pressed('h'):
        fun_ruka_down()
    else:
        stop()
'''
keyboard.add_hotkey('0', stop)

keyboard.add_hotkey('d', right)
keyboard.add_hotkey('a', left)
keyboard.add_hotkey('w', forward)
keyboard.add_hotkey('s', back)
keyboard.add_hotkey('t', fun_ruka_open)
keyboard.add_hotkey('g', fun_ruka_clouse)
keyboard.add_hotkey('f', fun_ruka_up)
keyboard.add_hotkey('h', fun_ruka_down)

keyboard.wait('Ctrl + Q')
'''
