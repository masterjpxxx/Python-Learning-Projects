#This python program decodes the QRcode passed from the user input
#Step 1: Install the pyzbar and pillow library
#Step 2: Ask for the location of the QR code to be decoded
#Step 3: Decode the QR Code
#Step 4: Display the result

from pyzbar.pyzbar import decode
from PIL import Image

def decodeQRcode(location):
    img = Image.open(location)
    result = decode(img)
    return result


location = input("Please indicate the location of the QR Code: ")
print(decodeQRcode(location))

