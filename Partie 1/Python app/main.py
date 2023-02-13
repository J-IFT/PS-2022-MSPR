from tkinter import *
from PIL import Image, ImageTk
from function import display_logo, bandwidthtest, pingtest
import tkinter.font as font
import os

#root = la fenêtre

root = Tk()
root.title("SemaOS")
if "nt" == os.name:
    root.wm_iconbitmap(bitmap = "logo.ico")
else:
    root.wm_iconbitmap(bitmap = "@logo.xbm")
root.geometry("1500x720")
root.config(bg="white")
root.maxsize(1500, 720)

#header = pour le haut de la page

header = Frame(root, width=1500, height=300, bg="white")
header.grid(columnspan=3, rowspan=2, row=0)

#main_content = pour le corps de la page

main_content = Frame(root, width=1500, height=700, bg="#20bebe")
main_content.grid(columnspan=6,rowspan=6,row=2)

#pour le placement du logo
display_logo('logo.png', 0, 0)

btn = Button(root, text="Scan du réseau", fg="blue", command = lambda: quit(root))
btn1 = Button(root, text="Test de débit", fg="blue", command = lambda: bandwidthtest())
btn2 = Button(root, text="Test ping et latence", fg="blue", command = lambda: pingtest())
btn3 = Button(root, text="IP publique du client", fg="blue", command = lambda: quit(root))

#btn  1,2, etc... correspond au placement des boutons
btn.place(x=400, y=230)
btn1.place(x=600, y=230)
btn2.place(x=770, y=230)
btn3.place(x=980, y=230)

myFont = font.Font(family='Helvetica', size=10, weight='bold')
btn['font'] = myFont
btn1['font'] = myFont
btn2['font'] = myFont
btn3['font'] = myFont

label = Label(root, text="Adresse IP de la Semabox / Nom de la Semabox")
label1 = Label(root, text="IP publique de l'accès internet / Nom DNS dynamique")
label2 = Label(root, text="Etat de la connexion internet")
label3 = Label(root, text="Liste des machines détectées sur le réseau")
label4 = Label(root, text="Résultats du dernier test de débit")

#label  1,2, etc... correspond au placement des labels
label.place(x=50, y=350)
label1.place(x=350, y=350)
label2.place(x=680, y=350)
label3.place(x=880, y=350)
label4.place(x=1150, y=350)

root.mainloop()