'''
first we need to import smtp
we log into an existing acc then we use the smtp protocolwith the python scripts to
send mails from there
'''
from http import server
from operator import imod
import smtplib
from email import encoders, message
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart 
server = smtplib.SMTP('smtp.gmail.com', 465)
server.ehlo() #function needed to start the process

with open('pswd.txt', 'r') as f:
          pswd = f.read()

server.login('myprojects583@gmail.com', pswd)  

msg = MIMEMultipart()
msg['from'] = "Nyaradzo"
msg['To'] = 'nchinyati20@gmail.com'
msg['Subject'] = 'KEEP ON KEEPING ON'

with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))


text = msg.as_string()
server.sendmail('myprojects583@gmail.com','nchinyati20@gmail.com', text)
