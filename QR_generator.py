# Build a QR Code Generator using Python

# We are going to use a python library like qrcode and convert url to qr

import qrcode

url = input("Enter your url: ")
filename = input("File name you want to save it as: ")
if not (filename.endswith(".png")):
    filename += ".png"

img = qrcode.make(url)
img.save(filename)