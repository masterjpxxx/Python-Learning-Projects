#This python program 


import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

#Server declaration
server = smtplib.SMTP("smtp.gmail.com", 25)


#Email Variables
sender = "" #Enter sender email address here
receiver = "" #Enter receiver email address here

#initialize the server before sending the mail message
server.ehlo()

#open the password hidden in the password.txt file
with open("password.txt", 'r') as f:
    password = f.read()

#login using the credentials provided
server.login(sender, password)

#Mail headers
msg = MIMEMultipart
msg['From'] = "Pinoytechcentral"
msg['To'] = ""
msg['Subject'] = "Python Mailing Client Test"

#open the email message from the file message.txt
with open("message.txt", 'r') as f:
    message = f.read()
 
#Attach it to the msg object as plain text   
msg.attach(MIMEText(message, 'plain'))

#Make sure to save the attachment together with the python files and text files
filename = "img8.png"
#open file in readbyte mode
attachment = open(filename, 'rb')


p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())
encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')

#attach image to the msg objext
msg.attach(p)


text = msg.as_string()
#Send the actual e-mail 
server.sendmail(sender, receiver, text)
print("Message successfully sent!")

