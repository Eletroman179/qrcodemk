#!/usr/bin/env python

import qrcode 
import sys

def get_data():
    if sys.stdin.isatty():
        return input("qrcode data: ")
    else:
        # if piped, force interactive fallback
        print("qrcode data: ", end="", flush=True)
        return sys.stdin.readline().strip()

data = get_data()

img = qrcode.make(data)
print("saved qrcode as qrcode.png")
img.save("qrcode.png") # type: ignore