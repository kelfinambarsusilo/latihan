import random
import time;
import datetime
import tkinter.messagebox
from tkinter import*

root = Tk()
root.geometry("1350x750+0+0")
root.title("Restaurant Mangement System")
root.configure(background ='Cadet Blue')

Tops = Frame(root, bg='Cadet Blue', bd=20, pady=5, relief=RIDGE)
Tops.pack(side=TOP)
lblTitle =Label(Tops, font=('arial',60,'bold'),text="Aplikasi Kasir Enterprise Cafe",bd=21,bg='Cadet Blue',
                fg='Cornsilk',justify = CENTER)
lblTitle.grid(row=0,column=0)

ReceiptCal_F = Frame(root, bg='Powder Blue', bd=10, relief=RIDGE)
ReceiptCal_F.pack(side=RIGHT)

Buttons_F=Frame(ReceiptCal_F,bg='Powder Blue', bd=3, relief=RIDGE)
Buttons_F.pack(side=BOTTOM)

Cal_F=Frame(ReceiptCal_F,bg='Powder Blue', bd=6, relief=RIDGE)
Cal_F.pack(side=TOP)

Receipt_F=Frame(ReceiptCal_F,bg='Powder Blue', bd=4, relief=RIDGE)
Receipt_F.pack(side=BOTTOM)

MenuFrame = Frame(root, bg='Cadet Blue', bd=10, relief=RIDGE)
MenuFrame.pack(side=LEFT)
Cost_F=Frame(MenuFrame,bg='Powder Blue',bd=4)
Cost_F.pack(side=BOTTOM)
Drinks_F=Frame(MenuFrame, bg='Cadet Blue', bd=10)
Drinks_F.pack(side=TOP)

Drinks_F=Frame(MenuFrame, bg='Powder Blue', bd=10, relief=RIDGE)
Drinks_F.pack(side=LEFT)
Cake_F=Frame(MenuFrame,bg='Powder Blue',bd=10, relief=RIDGE)
Cake_F.pack(side=RIGHT)

#=======================================Variable================================================================================
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()

DateofOrder = StringVar()
Receipt_Ref = StringVar()
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
CostofCakes = StringVar()
CostofDrinks = StringVar()
ServiceCharge = StringVar()

text_Input = StringVar()
operator =""

E_Latta=StringVar()
E_Espresso=StringVar()
E_Iced_Latte=StringVar()
E_Vale_Coffee=StringVar()
E_Cappuccino=StringVar()
E_Arabica_Coffee=StringVar()
E_Solok_Coffee=StringVar()
E_Maluku_Coffee=StringVar()

E_Donat_Madu=StringVar()
E_Ulang_Tahun=StringVar()
E_Kue_Keju=StringVar()
E_Onde_Onde=StringVar()
E_Sarabi=StringVar()
E_Singgang_Bakar=StringVar()
E_Roti_Cane=StringVar()
E_Kebab_Turqei=StringVar()

E_Latta.set("0")
E_Espresso.set("0")
E_Iced_Latte.set("0")
E_Vale_Coffee.set("0")
E_Cappuccino.set("0")
E_Arabica_Coffee.set("0")
E_Solok_Coffee.set("0")
E_Maluku_Coffee.set("0")

E_Donat_Madu.set("0")
E_Ulang_Tahun.set("0")
E_Kue_Keju.set("0")
E_Onde_Onde.set("0")
E_Sarabi.set("0")
E_Singgang_Bakar.set("0")
E_Roti_Cane.set("0")
E_Kebab_Turqei.set("0")

DateofOrder.set(time.strftime("%d/%m/%y"))
#=======================================Functions==================================================================================

def iExit():
    iExit = tkinter.messagebox.askyesno("Exit Cafe Syatem","Yakin Mau EXIT?")
    if iExit>0:
        root.destroy()
        return
def Reset():
    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofDrinks.set("")
    CostofCakes.set("")
    ServiceCharge.set("")
    txtReceipt.delete("1.0",END)
    
    E_Latta.set("0")
    E_Espresso.set("0")
    E_Iced_Latte.set("0")
    E_Vale_Coffee.set("0")
    E_Cappuccino.set("0")
    E_Arabica_Coffee.set("0")
    E_Solok_Coffee.set("0")
    E_Maluku_Coffee.set("0")

    E_Donat_Madu.set("0")
    E_Ulang_Tahun.set("0")
    E_Kue_Keju.set("0")
    E_Onde_Onde.set("0")
    E_Sarabi.set("0")
    E_Singgang_Bakar.set("0")
    E_Roti_Cane.set("0")
    E_Kebab_Turqei.set("0")

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)

    txtLatta.configure(state =DISABLED)
    txtEspresso.configure(state =DISABLED)
    txtIced_Latte.configure(state =DISABLED)
    txtVale_Coffee.configure(state =DISABLED)
    txtCappuccino.configure(state =DISABLED)
    txtArabica_Coffee.configure(state =DISABLED)
    txtSolok_Coffee.configure(state =DISABLED)
    txtMaluku_Coffee.configure(state =DISABLED)
    txtDonat_Madu.configure(state =DISABLED)
    txtUlang_Tahun.configure(state =DISABLED)
    txtKue_Keju.configure(state =DISABLED)
    txtOnde_Onde.configure(state =DISABLED)
    txtSarabi.configure(state =DISABLED)
    txtSinggang_Bakar.configure(state =DISABLED)
    txtRoti_Cane.configure(state =DISABLED)
    txtKebab_Turqei.configure(state =DISABLED)

def CostofItem():
    Item1=float(E_Latta.get())
    Item2=float(E_Espresso.get())
    Item3=float(E_Iced_Latte.get())
    Item4=float(E_Vale_Coffee.get())
    Item5=float(E_Cappuccino.get())
    Item6=float(E_Arabica_Coffee.get())
    Item7=float(E_Solok_Coffee.get())
    Item8=float(E_Maluku_Coffee.get())

    Item9=float(E_Donat_Madu.get())
    Item10=float(E_Ulang_Tahun.get())
    Item11=float(E_Kue_Keju.get())
    Item12=float(E_Onde_Onde.get())
    Item13=float(E_Sarabi.get())
    Item14=float(E_Singgang_Bakar.get())
    Item15=float(E_Roti_Cane.get())
    Item16=float(E_Kebab_Turqei.get())

    PriceofDrinks = (Item1*10000)+(Item2*7000)+(Item3*8500)\
                    +(Item4*5000)+(Item5*7500)+(Item6*9000)+(Item7*8700)+(Item8*9800)

    PriceofCakes = (Item9*12000)+(Item10*11000)+(Item11*12500)\
                   +(Item12*10000)+(Item13*11500)+(Item14*15000)+(Item15*14000)+(Item16*13000)

    DrinksPrice = "Rp.", str('%.2f'%(PriceofDrinks))
    CakePrice = "Rp.",str('%.2f'%(PriceofCakes))
    CostofCakes.set(CakePrice)
    CostofDrinks.set(DrinksPrice)
    SC = "Rp.", str('%.2f'%(2000))
    ServiceCharge.set(SC)

    SubTotalofITEMS = "Rp.",str('%.2f'%(PriceofDrinks + PriceofCakes + 2000))
    SubTotal.set(SubTotalofITEMS)

    Tax = "Rp.", str('%.2f'%((PriceofDrinks + PriceofCakes + 2000)*0.10))
    PaidTax.set(Tax)
    TT = ((PriceofDrinks + PriceofCakes + 2000)*0.10)
    TC = "Rp.", str('%.2f'%(PriceofDrinks + PriceofCakes + 2000 + TT))
    TotalCost.set(TC)

def chkLatta():
    if(var1.get()== 1):
        txtLatta.configure(state = NORMAL)
        txtLatta.focus()
        txtLatta.delete('0', END)
        E_Latta.set("")
    elif(var1.get() == 0):
        txtLatta.configure(state = DISABLED)
        E_Latta.set("0") 
def chkEspresso():
    if(var2.get()== 1):
        txtEspresso.configure(state = NORMAL)
        txtEspresso.focus()
        txtEspresso.delete('0', END)
        E_Espresso.set("")
    elif(var2.get() == 0):
        txtEspresso.configure(state = DISABLED)
        E_Espresso.set("0")
def chkIced_Latte():
    if(var3.get()== 1):
        txtIced_Latte.configure(state = NORMAL)
        txtIced_Latte.focus()
        txtIced_Latte.delete('0', END)
        E_Iced_Latte.set("")
    elif(var3.get() == 0):
        txtIced_Latte.configure(state = DISABLED)
        E_Iced_Latte.set("0")
def chkVale_Coffee():
    if(var4.get()== 1):
        txtVale_Coffee.configure(state = NORMAL)
        txtVale_Coffee.focus()
        txtVale_Coffee.delete('0', END)
        E_Vale_Coffee.set("")
    elif(var4.get() == 0):
        txtVale_Coffee.configure(state = DISABLED)
        E_Vale_Coffee.set("0")
def chkCappuccino():
    if(var5.get()== 1):
        txtCappuccino.configure(state = NORMAL)
        txtCappuccino.focus()
        txtCappuccino.delete('0', END)
        E_Cappuccino.set("")
    elif(var5.get() == 0):
        txtCappuccino.configure(state = DISABLED)
        E_Cappuccino.set("0")
def chkArabica_Coffee():
    if(var6.get()== 1):
        txtArabica_Coffee.configure(state = NORMAL)
        txtArabica_Coffee.focus()
        txtArabica_Coffee.delete('0', END)
        E_Arabica_Coffee.set("")
    elif(var6.get() == 0):
        txtArabica_Coffee.configure(state = DISABLED)
        E_Arabica_Coffee.set("0")
def chkSolok_Coffee():
    if(var7.get()== 1):
        txtSolok_Coffee.configure(state = NORMAL)
        txtSolok_Coffee.focus()
        txtSolok_Coffee.delete('0', END)
        E_Solok_Coffee.set("")
    elif(var7.get() == 0):
        txtSolok_Coffee.configure(state = DISABLED)
        E_Solok_Coffee.set("0")
def chkMaluku_Coffee():
    if(var8.get()== 1):
        txtMaluku_Coffee.configure(state = NORMAL)
        txtMaluku_Coffee.focus()
        txtMaluku_Coffee.delete('0', END)
        E_Maluku_Coffee.set("")
    elif(var8.get() == 0):
        txtMaluku_Coffee.configure(state = DISABLED)
        E_Maluku_Coffee.set("0")
def chkDonat_Madu():
    if(var9.get()== 1):
        txtDonat_Madu.configure(state = NORMAL)
        txtDonat_Madu.focus()
        txtDonat_Madu.delete('0', END)
        E_Donat_Madu.set("")
    elif(var9.get() == 0):
        txtDonat_Madu.configure(state = DISABLED)
        E_Donat_Madu.set("0")
def chkUlang_Tahun():
    if(var10.get()== 1):
        txtUlang_Tahun.configure(state = NORMAL)
        txtUlang_Tahun.focus()
        txtUlang_Tahun.delete('0', END)
        E_Ulang_Tahun.set("")
    elif(var10.get() == 0):
        txtUlang_Tahun.configure(state = DISABLED)
        E_Ulang_Tahun.set("0")
def chkKue_Keju():
    if(var11.get()== 1):
        txtKue_Keju.configure(state = NORMAL)
        txtKue_Keju.focus()
        txtKue_Keju.delete('0', END)
        E_Kue_Keju.set("")
    elif(var11.get() == 0):
        txtKue_Keju.configure(state = DISABLED)
        E_Kue_Keju.set("0")
def chkOnde_Onde():
    if(var12.get()== 1):
        txtOnde_Onde.configure(state = NORMAL)
        txtOnde_Onde.focus()
        txtOnde_Onde.delete('0', END)
        E_Onde_Onde.set("")
    elif(var12.get() == 0):
        txtOnde_Onde.configure(state = DISABLED)
        E_Onde_Onde.set("0")
def chkSarabi():
    if(var13.get()== 1):
        txtSarabi.configure(state = NORMAL)
        txtSarabi.focus()
        txtSarabi.delete('0', END)
        E_Sarabi.set("")
    elif(var13.get() == 0):
        txtSarabi.configure(state = DISABLED)
        E_Sarabi.set("0")
def chkSinggang_Bakar():
    if(var14.get()== 1):
        txtSinggang_Bakar.configure(state = NORMAL)
        txtSinggang_Bakar.focus()
        txtSinggang_Bakar.delete('0', END)
        E_Singgang_Bakar.set("")
    elif(var14.get() == 0):
        txtSinggang_Bakar.configure(state = DISABLED)
        E_Singgang_Bakar.set("0")
def chkRoti_Cane():
    if(var15.get()== 1):
        txtRoti_Cane.configure(state = NORMAL)
        txtRoti_Cane.focus()
        txtRoti_Cane.delete('0', END)
        E_Roti_Cane.set("")
    elif(var15.get() == 0):
        txtRoti_Cane.configure(state = DISABLED)
        E_Roti_Cane.set("0")
def chkKebab_Turqei():
    if(var16.get()== 1):
        txtKebab_Turqei.configure(state = NORMAL)
        txtKebab_Turqei.focus()
        txtKebab_Turqei.delete('0', END)
        E_Kebab_Turqei.set("")
    elif(var16.get() == 0):
        txtKebab_Turqei.configure(state = DISABLED)
        E_Kebab_Turqei.set("0")
def Receipt():
    txtReceipt.delete("1.0", END)
    x = random.randint(10903, 609235)
    randomRef = str(x)
    Receipt_Ref.set("BILL" + randomRef)

    txtReceipt.insert(END, 'Receipt Ref:\t\t\t'+ Receipt_Ref.get() +'\t'+DateofOrder.get()+"\n")
    txtReceipt.insert(END, 'Item:\t\t\t'+ "Cost of Items\n")
    txtReceipt.insert(END, 'Latta:\t\t\t'+E_Latta.get()+"\n")
    txtReceipt.insert(END, 'Espresso:\t\t\t'+E_Espresso.get()+"\n")
    txtReceipt.insert(END, 'Iced_Latte:\t\t\t'+E_Iced_Latte.get()+"\n")
    txtReceipt.insert(END, 'Vale_Coffee:\t\t\t'+E_Vale_Coffee.get()+"\n")
    txtReceipt.insert(END, 'Cappuccino:\t\t\t'+E_Cappuccino.get()+"\n")
    txtReceipt.insert(END, 'Arabica_Coffee:\t\t\t'+E_Arabica_Coffee.get()+"\n")
    txtReceipt.insert(END, 'Solok_Coffee:\t\t\t'+E_Solok_Coffee.get()+"\n")
    txtReceipt.insert(END, 'Maluku_Coffee:\t\t\t'+E_Maluku_Coffee.get()+"\n")
    txtReceipt.insert(END, 'Donat_Madu:\t\t\t'+E_Donat_Madu.get()+"\n")
    txtReceipt.insert(END, 'Ulang_Tahun:\t\t\t'+E_Ulang_Tahun.get()+"\n")
    txtReceipt.insert(END, 'Kue_Keju:\t\t\t'+E_Kue_Keju.get()+"\n")
    txtReceipt.insert(END, 'Onde_Onde:\t\t\t'+E_Onde_Onde.get()+"\n")
    txtReceipt.insert(END, 'Sarabi:\t\t\t'+E_Sarabi.get()+"\n")
    txtReceipt.insert(END, 'Singgang_Bakar:\t\t\t'+E_Singgang_Bakar.get()+"\n")
    txtReceipt.insert(END, 'Roti_Cane:\t\t\t'+E_Roti_Cane.get()+"\n")
    txtReceipt.insert(END, 'Kebab_Turqei:\t\t\t'+E_Kebab_Turqei.get()+"\n")
    txtReceipt.insert(END, 'Harga Minuman:\t\t\t'+CostofDrinks.get()+'\nPPN :\t\t\t\t'+ PaidTax.get()+"\n")
    txtReceipt.insert(END, 'Harga Makanan:\t\t\t'+CostofCakes.get()+'\nSubTotal:\t\t\t\t'+ str(SubTotal.get())+"\n")
    txtReceipt.insert(END, 'Service Charge:\t\t\t'+ServiceCharge.get()+'\nTotal Cost:\t\t\t\t'+ str(TotalCost.get()))
    

#=======================================Drinks================================================================================

Latta =Checkbutton(Drinks_F, text="Latte", variable=var1, onvalue =1, offvalue=0,font=('arial',18,'bold'),
                   bg='Powder Blue', command = chkLatta).grid(row=0, sticky=W)
Espresso =Checkbutton(Drinks_F, text="Espresso", variable=var2, onvalue =1, offvalue=0,font=('arial',18,'bold'),
                   bg='Powder Blue',command = chkEspresso).grid(row=1, sticky=W)
Iced_Latte =Checkbutton(Drinks_F, text="Iced Latte", variable=var3, onvalue =1, offvalue=0,font=('arial',18,'bold'),
                   bg='Powder Blue',command = chkIced_Latte).grid(row=2, sticky=W)
Vale_Coffee =Checkbutton(Drinks_F, text="Vale Coffee", variable=var4, onvalue =1, offvalue=0,font=('arial',18,'bold'),
                   bg='Powder Blue',command = chkVale_Coffee).grid(row=3, sticky=W)
Cappuccino =Checkbutton(Drinks_F, text="Cappuccino", variable=var5, onvalue =1, offvalue=0,font=('arial',18,'bold'),
                   bg='Powder Blue',command = chkCappuccino).grid(row=4, sticky=W)
Arabica_Coffee =Checkbutton(Drinks_F, text="Arabica Coffe", variable=var6, onvalue =1, offvalue=0,font=('arial',18,'bold'),
                   bg='Powder Blue',command = chkArabica_Coffee).grid(row=5, sticky=W)
Solok_Coffee =Checkbutton(Drinks_F, text="Solok Coffee", variable=var7, onvalue =1, offvalue=0,font=('arial',18,'bold'),
                   bg='Powder Blue',command = chkSolok_Coffee).grid(row=6, sticky=W)
Maluku_Coffee =Checkbutton(Drinks_F, text="Maluku Coffee", variable=var8, onvalue =1, offvalue=0,font=('arial',18,'bold'),
                   bg='Powder Blue',command = chkMaluku_Coffee).grid(row=7, sticky=W)
#=======================================Entry Box for Drinks==================================================================

txtLatta = Entry(Drinks_F,font=('arial',16,'bold'),textvariable=E_Latta, bd=8, width=6, justify=LEFT, state = DISABLED)
txtLatta.grid(row=0,column=1)

txtEspresso = Entry(Drinks_F,font=('arial',16,'bold'),textvariable=E_Espresso, bd=8, width=6, justify=LEFT, state = DISABLED)
txtEspresso.grid(row=1,column=1)

txtIced_Latte = Entry(Drinks_F,font=('arial',16,'bold'),textvariable=E_Iced_Latte, bd=8, width=6, justify=LEFT, state = DISABLED)
txtIced_Latte.grid(row=2,column=1)

txtVale_Coffee = Entry(Drinks_F,font=('arial',16,'bold'),textvariable=E_Vale_Coffee, bd=8, width=6, justify=LEFT, state = DISABLED)
txtVale_Coffee.grid(row=3,column=1)

txtCappuccino = Entry(Drinks_F,font=('arial',16,'bold'),textvariable=E_Cappuccino, bd=8, width=6, justify=LEFT, state = DISABLED)
txtCappuccino.grid(row=4,column=1)

txtArabica_Coffee = Entry(Drinks_F,font=('arial',16,'bold'),textvariable=E_Arabica_Coffee, bd=8, width=6, justify=LEFT, state = DISABLED)
txtArabica_Coffee.grid(row=5,column=1)

txtSolok_Coffee = Entry(Drinks_F,font=('arial',16,'bold'),textvariable=E_Solok_Coffee, bd=8, width=6, justify=LEFT, state = DISABLED)
txtSolok_Coffee.grid(row=6,column=1)

txtMaluku_Coffee= Entry(Drinks_F,font=('arial',16,'bold'),textvariable=E_Maluku_Coffee, bd=8, width=6, justify=LEFT, state = DISABLED)
txtMaluku_Coffee.grid(row=7,column=1)
#=======================================Cakes=================================================================================

Donat_Madu =Checkbutton(Cake_F, text="Donat Madu\t\t\t ", variable=var9, onvalue =1, offvalue=0,
                    font=('arial',16,'bold'),
                   bg='Powder Blue',command = chkDonat_Madu).grid(row=0, sticky=W)
Ulang_Tahun =Checkbutton(Cake_F, text="Ulang Tahun", variable=var10, onvalue =1, offvalue=0,
                    font=('arial',16,'bold'),
                   bg='Powder Blue',command = chkUlang_Tahun).grid(row=1, sticky=W)
Kue_Keju =Checkbutton(Cake_F, text="Kue Keju", variable=var11, onvalue =1, offvalue=0,
                    font=('arial',16,'bold'),
                   bg='Powder Blue',command = chkKue_Keju).grid(row=2, sticky=W)
Onde_Onde =Checkbutton(Cake_F, text="Onde Onde", variable=var12, onvalue =1, offvalue=0,
                    font=('arial',16,'bold'),
                   bg='Powder Blue',command = chkOnde_Onde).grid(row=3, sticky=W)
Sarabi =Checkbutton(Cake_F, text="Sarabi", variable=var13, onvalue =1, offvalue=0,
                    font=('arial',16,'bold'),
                   bg='Powder Blue',command = chkSarabi).grid(row=4, sticky=W)
Singgang_Bakar =Checkbutton(Cake_F, text="Singgang Bakar", variable=var14, onvalue =1, offvalue=0,
                    font=('arial',16,'bold'),
                   bg='Powder Blue',command = chkSinggang_Bakar).grid(row=5, sticky=W)
Roti_Cane =Checkbutton(Cake_F, text="Roti Cane", variable=var15, onvalue =1, offvalue=0,
                    font=('arial',16,'bold'),
                   bg='Powder Blue',command = chkRoti_Cane).grid(row=6, sticky=W)
Kebab_Turqei =Checkbutton(Cake_F, text="Kebab Turqei", variable=var16, onvalue =1, offvalue=0,
                    font=('arial',16,'bold'),
                   bg='Powder Blue',command = chkKebab_Turqei).grid(row=7, sticky=W)

#=======================================Entry Box for Cakes==================================================================

txtDonat_Madu = Entry(Cake_F,font=('arial',16,'bold'), bd=8, width=6, justify=LEFT,
                      state = DISABLED,textvariable=E_Donat_Madu)
txtDonat_Madu.grid(row=0,column=1)

txtUlang_Tahun = Entry(Cake_F,font=('arial',16,'bold'), bd=8, width=6, justify=LEFT,
                       state = DISABLED,textvariable=E_Ulang_Tahun)
txtUlang_Tahun.grid(row=1,column=1)

txtKue_Keju = Entry(Cake_F,font=('arial',16,'bold'), bd=8, width=6, justify=LEFT,
                    state = DISABLED,textvariable=E_Kue_Keju)
txtKue_Keju.grid(row=2,column=1)

txtOnde_Onde = Entry(Cake_F,font=('arial',16,'bold'), bd=8, width=6, justify=LEFT,
                     state = DISABLED,textvariable=E_Onde_Onde)
txtOnde_Onde.grid(row=3,column=1)

txtSarabi = Entry(Cake_F,font=('arial',16,'bold'), bd=8, width=6, justify=LEFT,
                  state = DISABLED,textvariable=E_Sarabi)
txtSarabi.grid(row=4,column=1)

txtSinggang_Bakar = Entry(Cake_F,font=('arial',16,'bold'), bd=8, width=6, justify=LEFT,
                          state = DISABLED,textvariable=E_Singgang_Bakar)
txtSinggang_Bakar.grid(row=5,column=1)

txtRoti_Cane = Entry(Cake_F,font=('arial',16,'bold'), bd=8, width=6, justify=LEFT,
                     state = DISABLED,textvariable=E_Roti_Cane)
txtRoti_Cane.grid(row=6,column=1)

txtKebab_Turqei = Entry(Cake_F,font=('arial',16,'bold'), bd=8, width=6, justify=LEFT,
                        state = DISABLED,textvariable=E_Kebab_Turqei)
txtKebab_Turqei.grid(row=7,column=1)

#===========================================Total Cost==========================================================================

lblCostofDrinks = Label(Cost_F,font=('arial', 14,'bold'),text="Harga Minuman\t  ", bg="powder Blue",fg="black")
lblCostofDrinks.grid(row=0,column=0,sticky=W)
txtCostofDrinks = Entry(Cost_F,font=('arial',14,'bold'),textvariable=CostofDrinks, bd=7, bg="white",
                        insertwidth=2,justify=RIGHT)
txtCostofDrinks.grid(row=0,column=1)

lblCostofCakes = Label(Cost_F,font=('arial', 14,'bold'),text="Harga Makanan", bg="powder Blue",fg="black")
lblCostofCakes.grid(row=1,column=0,sticky=W)
txtCostofCakes = Entry(Cost_F,font=('arial',14,'bold'),textvariable=CostofCakes, bd=7, bg="white",
                        insertwidth=2,justify=RIGHT)
txtCostofCakes.grid(row=1,column=1)

lblServiceCharge = Label(Cost_F,font=('arial', 14,'bold'),text="Service Charge", bg="powder Blue",fg="black")
lblServiceCharge.grid(row=2,column=0,sticky=W)
txtServiceCharge = Entry(Cost_F,font=('arial',14,'bold'),textvariable=ServiceCharge, bd=7, bg="white",
                        justify=RIGHT)
txtServiceCharge.grid(row=2,column=1)

#===========================================Payment Information==========================================================================
lblPaidTax = Label(Cost_F,font=('arial', 14,'bold'),text="\tPPN\t  ", bg="powder Blue",fg="black")
lblPaidTax.grid(row=0,column=2,sticky=W)
txtPaidTax = Entry(Cost_F,font=('arial',14,'bold'),textvariable=PaidTax, bd=7, bg="white",
                        insertwidth=2,justify=RIGHT)
txtPaidTax.grid(row=0,column=3)

lblSubTotal = Label(Cost_F,font=('arial',14,'bold'),text="\tSub Total", bg="powder Blue",fg="black")
lblSubTotal.grid(row=1,column=2,sticky=W)
txtSubTotal = Entry(Cost_F,font=('arial',14,'bold'),textvariable=SubTotal,bd=7, bg="white",
                        insertwidth=2,justify=RIGHT)
txtSubTotal.grid(row=1,column=3)

lblTotalCost = Label(Cost_F,font=('arial', 14,'bold'),text="\tTotal Harga", bg="powder Blue",fg="black")
lblTotalCost.grid(row=2,column=2,sticky=W)
txtTotalCost = Entry(Cost_F,font=('arial',14,'bold'),textvariable=TotalCost,bd=7, bg="white",
                        insertwidth=2,justify=RIGHT)
txtTotalCost.grid(row=2,column=3)


#===========================================Receipt==========================================================================

txtReceipt = Text(Receipt_F, width=46, height=12, bg="white",bd=4,font=('arial',12,'bold'))
txtReceipt.grid(row=0,column=0)

#===========================================Buttons==========================================================================

btnTotal=Button(Buttons_F, padx=16, pady=1, bd=7, fg="black", font=('arial',16,'bold'), width=4, text="Total",
                bg='powder Blue',command = CostofItem).grid(row=0, column=0)
btnReceipt=Button(Buttons_F, padx=16, pady=1, bd=7, fg="black", font=('arial',16,'bold'), width=4, text="Receipt",
                bg='powder Blue',command = Receipt).grid(row=0, column=1)
btnReset=Button(Buttons_F, padx=16, pady=1, bd=7, fg="black", font=('arial',16,'bold'), width=4, text="Reset",
                bg='powder Blue',command= Reset).grid(row=0, column=2)
btnExit=Button(Buttons_F, padx=16, pady=1, bd=7, fg="black", font=('arial',16,'bold'), width=4, text="Exit",
                bg='powder Blue',command = iExit).grid(row=0, column=3)

#===========================================Calculator Display==========================================================================
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClear():
    global operator
    operator = ""
    text_Input.set("")

def btnEquals():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""

txtDisplay = Entry(Cal_F, width=46, bg="white",bd=4,font=('arial',12,'bold'), justify=RIGHT,textvariable=text_Input)
txtDisplay.grid(row=0,column=0,columnspan=4, pady=1)
txtDisplay.insert(0,"0")

#===========================================Calculator Buttons==========================================================================

btn7=Button(Cal_F, padx=16, pady=1, bd=7, fg="black", font=('arial',16,'bold'), width=4, text="7",
                bg='powder Blue',command=lambda:btnClick(7)).grid(row=2, column=0)
btn8=Button(Cal_F, padx=16, pady=1, bd=7, fg="black", font=('arial',16,'bold'), width=4, text="8",
                bg='powder Blue',command=lambda:btnClick(8)).grid(row=2, column=1)
btn9=Button(Cal_F, padx=16, pady=1, bd=7, fg="black", font=('arial',16,'bold'), width=4, text="9",
                bg='powder Blue',command=lambda:btnClick(9)).grid(row=2, column=2)
btnAdd=Button(Cal_F, padx=16, pady=1, bd=7, fg="black", font=('arial',16,'bold'), width=4, text="+",
                bg='powder Blue',command=lambda:btnClick("+")).grid(row=2, column=3)
#===========================================Calculator Buttons==========================================================================

btn4=Button(Cal_F, padx=16, pady=1, bd=7, fg="black", font=('arial',16,'bold'), width=4, text="4",
                bg='powder Blue',command=lambda:btnClick(4)).grid(row=3, column=0)
btn5=Button(Cal_F, padx=16, pady=1, bd=7, fg="black", font=('arial',16,'bold'), width=4, text="5",
                bg='powder Blue',command=lambda:btnClick(5)).grid(row=3, column=1)
btn6=Button(Cal_F, padx=16, pady=1, bd=7, fg="black", font=('arial',16,'bold'), width=4, text="6",
                bg='powder Blue',command=lambda:btnClick(6)).grid(row=3, column=2)
btnSub=Button(Cal_F, padx=16, pady=1, bd=7, fg="black", font=('arial',16,'bold'), width=4, text="-",
                bg='powder Blue',command=lambda:btnClick("-")).grid(row=3, column=3)
#===========================================Calculator Buttons==========================================================================

btn1=Button(Cal_F, padx=16, pady=1, bd=7, fg="black", font=('arial',16,'bold'), width=4, text="1",
                bg='powder Blue',command=lambda:btnClick(1)).grid(row=4, column=0)
btn2=Button(Cal_F, padx=16, pady=1, bd=7, fg="black", font=('arial',16,'bold'), width=4, text="2",
                bg='powder Blue',command=lambda:btnClick(2)).grid(row=4, column=1)
btn3=Button(Cal_F, padx=16, pady=1, bd=7, fg="black", font=('arial',16,'bold'), width=4, text="3",
                bg='powder Blue',command=lambda:btnClick(3)).grid(row=4, column=2)
btnMulti=Button(Cal_F, padx=16, pady=1, bd=7, fg="black", font=('arial',16,'bold'), width=4, text="*",
                bg='powder Blue',command=lambda:btnClick("*")).grid(row=4, column=3)
#===========================================Calculator Buttons==========================================================================

btn0=Button(Cal_F, padx=16, pady=1, bd=7, fg="black", font=('arial',16,'bold'), width=4, text="0",
                bg='powder Blue',command=lambda:btnClick(0)).grid(row=5, column=0)
btnClear=Button(Cal_F, padx=16, pady=1, bd=7, fg="black", font=('arial',16,'bold'), width=4, text="C",
                bg='powder Blue',command=btnClear).grid(row=5, column=1)
btnEquals=Button(Cal_F, padx=16, pady=1, bd=7, fg="black", font=('arial',16,'bold'), width=4, text="=",
                bg='powder Blue',command=btnEquals).grid(row=5, column=2)
btnDiv=Button(Cal_F, padx=16, pady=1, bd=7, fg="black", font=('arial',16,'bold'), width=4, text="/",
                bg='powder Blue',command=lambda:btnClick("/")).grid(row=5, column=3)


root.mainloop()
 
