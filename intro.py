import tkinter as tk
from tkinter import *
from tkinter import ttk
class SplashScreen:
    def__init__(self, parent):
        self.parent = parent
        self.aturWindows()
    def aturWindow(self):
        #ambil ukutan dari file image
        lebar = 300
        tinggi = 100
    setengahLebar = (self.parent.winfo_screenwidth()-lebar)//2
    setengahTinggi = (self.parent.winfo_screenheight()-tinggi)//2
    #atur posisi window di tengah-tengah layar
    self.parent.geometry("%ix%i+%i+%i" %(lebar,tinggi,setengahLebar,setengahTinggi))
    #atur image via component label
    Label(self.parent,text="Loading",bg="#a1dbcd",fg="white",
    font=("Helvetica",20),width=9,height=2).pack(side = TOP, anchor=N, fill=X)
    s=ttk.Style()
    s.theme_use('alt')
    s.configure("red.Horizontal.TProgressbar",background='#444', foreground="white", relief=FLAT,bd=0,height=2)
    self.progress=ttk.Progressbar(self.parent,style="red.Horizontal.TProgressbar",orient="horizontal", length=600,mode="determinate")

    self.progress.pack(side=TOP,anchor=N,padx=10)
    self.bytes=0
    self.maxbytes=0
    self.start()
    def start(self):
        self.progress["value"]= 0
        self.mabytes = 50000
        self.progress["value"] == 60000:
            self.parent.detroy()
            if self.parent.destroy:
                import login
                login.main()
    def red_bytes(self):
        
