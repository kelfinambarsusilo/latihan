import random
import time;
import datetime
import tkinter.messagebox
from tkinter import*

root = Tk()
root.geometry("1350x750+0+0")
root.title("Restaurant Management System")
root.configure(background ='Cadet Blue')

Tops = Frame(root, bg='Cadet Blue', bd=20, pady=5, relief=RIDGE)
Tops.pack(side=TOP)

MenuFrame = Frame(root, bg='Cadet Blue', bd=10, relief=RIDGE)
MenuFrame.pack(side=LEFT)

ReceiptCal_F = Frame(root, bg='Powder Blue', bd=10, relief=RIDGE)
ReceiptCal_F.pack(side=RIGHT)

root.mainloop()