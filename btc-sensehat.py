#! /usr/bin/python2.7

import sys
from time import sleep
from blockchain import blockexplorer
from sense_hat import SenseHat

add = str(sys.argv[1])

sense = SenseHat()
r = (255,0,0)
b = (0,0,0) #black not blue
g = (0,255,0)
w = (255,255,255)

nope = [
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, r
]

black = [
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b
]

white = [
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w
]

yep = [
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g
    ]

def checkbalance():
    val = blockexplorer.get_address(add)
    realval = float(val.final_balance)/100000000
    return realval;

while True:
    val = checkbalance()

#rip your retinas
    if val > 0:
        for i in range(0,100000):
            sense.set_pixels(yep)
            sleep(0.05)
            sense.set_pixels(white)
            sleep(0.05)
            sense.set_pixels(black)
            sleep(0.05)
        exit()

    else:
        sense.set_pixels(nope)
        exit()
