#!/usr/bin/env python

import qrcode 

img = qrcode.make(input("qrcode data: "))
print("saved qrcode as qrcode.png")
img.save("qrcode.png") # type: ignore