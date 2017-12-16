#!/usr/bin/python

import sys
from blockchain import blockexplorer
from sense_hat import SenseHat
from time import sleep

add = str(sys.argv[1])
print "watching", add, "for balance"

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
    print val

    if val > 0:
        print "must have found a block"
        for i in range(0,100000):
            sense.set_pixels(yep)
            sleep(0.05)
            sense.set_pixels(white)
            sleep(0.05)
        exit()

    else:
        print "nope, keep digging"
        sense.set_pixels(nope)

    sleep(600)
