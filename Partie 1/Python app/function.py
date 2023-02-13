from tkinter import *
from PIL import Image, ImageTk
import subprocess
import os

def quit(root):
    root.destroy
    
def display_logo(url, row, column):
    img = Image.open(url)
    img = img.resize((int(img.size[0]/1.5),int(img.size[1]/1.5)))
    img = ImageTk.PhotoImage(img)
    img_label = Label(image=img, bg="white")
    img_label.image = img
    img_label.grid(column=column, row=row, rowspan=2, sticky=NW, padx=20, pady=40)

def scan():
    pass

def bandwidthtest():
    # subprocess.run("speedtest --format=json")
    print('test ok')
    pass

def pingtest():
    os.system('ping -c 1 www.google.fr')
    pass

def getIp():
    pass