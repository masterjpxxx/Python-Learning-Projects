#This python program creates a QR code based on the data inputted
#Step1: Install qr code library
#Step2: Ask for data from the user
#Step3: Ask for the destination of the QR code to be generated
#Step4: Generate QR code from the data

import qrcode
import os, random



def generateqr(data, location):
    
    check = os.path.exists(location)
    filename=""
    filenamechars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
 
    for j in range(8):
        filename += random.choice(filenamechars)
        
    if check:
        qr = qrcode.QRCode(version = 1,error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        qr.add_data(data)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(location+filename+".png")
        print("Qrcode generated successfully!")
    else:
        print("Invalid Location! Please try again!")
    

data = input("Please input data to be converted to QRCode: ")
location = input("Where do you want to save the QRcode: ")

generateqr(data, location)