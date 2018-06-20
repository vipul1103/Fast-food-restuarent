from tkinter import *
import random
import time
import datetime
from tkinter import Tk,StringVar,ttk,messagebox

root=Tk()
root.geometry("1350x750+0+0")
root.title("Fast Food Restaurant")

tops=Frame(root,width=1350,height=100,bd=12,relief="raise")
tops.pack(side=TOP)
lbltitle=Label(tops,font=('arial',50,'bold'),text="\tFast Food Restaurant\t\t\t")
lbltitle.grid(row=0,column=0)

bottommainframe=Frame(root,width=1350,height=650,bd=12,relief="raise")
bottommainframe.pack(side=BOTTOM)

f1=Frame(bottommainframe,width=450,height=650,bd=12,relief="raise")
f1.pack(side=LEFT)
f2=Frame(bottommainframe,width=450,height=650,bd=12,relief="raise")
f2.pack(side=LEFT)
f2top=Frame(f2,width=450,height=350,bd=6,relief="raise")
f2top.pack(side=TOP)
f2bottom=Frame(f2,width=450,height=300,bd=6,relief="raise")
f2bottom.pack(side=BOTTOM)
f3=Frame(bottommainframe,width=450,height=650,bd=12,relief="raise")
f3.pack(side=RIGHT)

var1=IntVar()
var1.set(0)
var2=IntVar()
var2.set(0)
var3=IntVar()
var3.set(0)
var4=IntVar()
var4.set(0)
var5=IntVar()
var5.set(0)
var6=IntVar()
var6.set(0)
var7=IntVar()
var7.set(0)
var8=IntVar()
var8.set(0)
var9=IntVar()
var9.set(0)
var10=IntVar()
var10.set(0)
var11=IntVar()
var11.set(0)
var12=IntVar()
var12.set(0)
var13=IntVar()
var13.set(0)
var14=IntVar()
var14.set(0)
var15=IntVar()
var15.set(0)
var16=IntVar()
var16.set(0)
var17=IntVar()
var17.set(0)
var18=IntVar()
var18.set(0)
var19=IntVar()
var19.set(0)
var20=IntVar()
var20.set(0)
var21=IntVar()
var21.set(0)
var22=StringVar()
var22.set("")
var23=IntVar()
var23.set("")
varFries=StringVar()
varFries.set("0")
varSalad=StringVar()
varSalad.set("0")
varHamburger=StringVar()
varHamburger.set("0")
varOnionrings=StringVar()
varOnionrings.set("0")
varChickensalad=StringVar()
varChickensalad.set("0")
varFishsandwich=StringVar()
varFishsandwich.set("0")
varCheesesandwich=StringVar()
varCheesesandwich.set("0")
varChikensandwich=StringVar()
varChikensandwich.set("0")

varHashBrown=StringVar()
varHashBrown.set("0")
varToastedBagel=StringVar()
varToastedBagel.set("0")
varPancakesSyrup=StringVar()
varPancakesSyrup.set("0")
varPineappleStick=StringVar()
varPineappleStick.set("0")
varChacolateMuffin=StringVar()
varChacolateMuffin.set("0")

varTea=StringVar()
varTea.set("0")
varCola=StringVar()
varCola.set("0")
varCoffee=StringVar()
varCoffee.set("0")
varWaterBottle=StringVar()
varWaterBottle.set("0")
varOrange=StringVar()
varOrange.set("0")
varVanillaCone=StringVar()
varVanillaCone.set("0")
varVanillaShake=StringVar()
varVanillaShake.set("0")
varStrawberryShake=StringVar()
varStrawberryShake.set("0")

varChange=StringVar()
varChange.set("0")
varTax=StringVar()
varTax.set("0")
varPayment=IntVar()
varPayment.set(" ")

varSubTotal=StringVar()
varSubTotal.set("0")
varTotal=StringVar()
varTotal.set("0")

def iExit():
    qExit=messagebox.askyesno("Fast Food","Do You Want To Quit?")
    if qExit > 0:
        root.destroy()
        return

def Reset():
    varFries.set("0")
    varSalad.set("0")
    varHamburger.set("0")
    varOnionrings.set("0")
    varChickensalad.set("0")
    varFishsandwich.set("0")
    varCheesesandwich.set("0")
    varChikensandwich.set("0")
 
    varHashBrown.set("0")
    varToastedBagel.set("0")
    varPancakesSyrup.set("0")
    varPineappleStick.set("0")
    varChacolateMuffin.set("0")
 
    varTea.set("0")
    varCola.set("0")
    varCoffee.set("0")
    varWaterBottle.set("0")
    varOrange.set("0")
    varVanillaCone.set("0")
    varVanillaShake.set("0")
    varStrawberryShake.set("0")
    varPayment.set(" ")
    varChange.set("0")
    varTax.set("0")
    varSubTotal.set("0")
    varTotal.set("0")

    txtFries.configure(state=DISABLED)
    txtSalad.configure(state=DISABLED)
    txtHamburger.configure(state=DISABLED)
    txtOnionrings.configure(state=DISABLED)
    txtChickensalad.configure(state=DISABLED)
    txtFishsandwich.configure(state=DISABLED)
    txtCheesesandwich.configure(state=DISABLED)
    txtChikensandwich.configure(state=DISABLED)
 
    txtHashBrown.configure(state=DISABLED)
    txtToastedBagel.configure(state=DISABLED)
    txtPancakesSyrup.configure(state=DISABLED)
    txtPineappleStick.configure(state=DISABLED)
    txtChacolateMuffin.configure(state=DISABLED)

    txtTea.configure(state=DISABLED)
    txtCola.configure(state=DISABLED)
    txtCoffee.configure(state=DISABLED)
    txtWaterBottle.configure(state=DISABLED)
    txtOrange.configure(state=DISABLED)
    txtVanillaCone.configure(state=DISABLED)
    txtVanillaShake.configure(state=DISABLED)
    txtStrawberryShake.configure(state=DISABLED)

    txtChange.configure(state=DISABLED)
    txtTax.configure(state=DISABLED)
    #txtPayment.configure(state=DISABLED)
    txtSubTotal.configure(state=DISABLED)
    txtTotal.configure(state=DISABLED)


def checkFries():
    if(var1.get()==1):
        txtFries.configure(state=NORMAL)
        varFries.set("")
    elif(var1.get()==0):
        txtFries.configure(state=DISABLED)
        varFries.set("0")

def checkSalad():
    if(var2.get()==1):
        txtSalad.configure(state=NORMAL)
        varSalad.set("")
    elif(var2.get()==0):
        txtSalad.configure(state=DISABLED)
        varSalad.set("0")

def checkHamburger():
    if(var3.get()==1):
        txtHamburger.configure(state=NORMAL)
        varHamburger.set("")
    elif(var3.get()==0):
        txtHamburger.configure(state=DISABLED)
        varHamburger.set("0")

def checkOnionrings():
    if(var4.get()==1):
        txtOnionrings.configure(state=NORMAL)
        varOnionrings.set("")
    elif(var4.get()==0):
        txtOnionrings.configure(state=DISABLED)
        varOnionrings.set("0")

def checkChickensalad():
    if(var5.get()==1):
        txtChickensalad.configure(state=NORMAL)
        varChickensalad.set("")
    elif(var5.get()==0):
        txtChickensalad.configure(state=DISABLED)
        varChickensalad.set("0")

def checkFishsandwich():
    if(var6.get()==1):
        txtFishsandwich.configure(state=NORMAL)
        varFishsandwich.set("")
    elif(var6.get()==0):
        txtFishsandwich.configure(state=DISABLED)
        varFishsandwich.set("0")

def checkCheesesandwich():
    if(var7.get()==1):
        txtCheesesandwich.configure(state=NORMAL)
        varCheesesandwich.set("")
    elif(var7.get()==0):
        txtCheesesandwich.configure(state=DISABLED)
        varCheesesandwich.set("0")

def checkChikensandwich():
    if(var8.get()==1):
        txtChikensandwich.configure(state=NORMAL)
        varChikensandwich.set("")
    elif(var8.get()==0):
        txtChikensandwich.configure(state=DISABLED)
        varChikensandwich.set("0")

def checkHashBrown():
    if(var9.get()==1):
        txtHashBrown.configure(state=NORMAL)
        varHashBrown.set("")
    elif(var9.get()==0):
        txtHashBrown.configure(state=DISABLED)
        varHashBrown.set("0")

def checkToastedBagel():
    if(var10.get()==1):
        txtToastedBagel.configure(state=NORMAL)
        varToastedBagel.set("")
    elif(var10.get()==0):
        txtToastedBagel.configure(state=DISABLED)
        varToastedBagel.set("0")

def checkPancakesSyrup():
    if(var11.get()==1):
        txtPancakesSyrup.configure(state=NORMAL)
        varPancakesSyrup.set("")
    elif(var11.get()==0):
        txtPancakesSyrup.configure(state=DISABLED)
        varPancakesSyrup.set("0")

def checkPineappleStick():
    if(var12.get()==1):
        txtPineappleStick.configure(state=NORMAL)
        varPineappleStick.set("")
    elif(var12.get()==0):
        txtPineappleStick.configure(state=DISABLED)
        varPineappleStick.set("0")

def checkChacolateMuffin():
    if(var13.get()==1):
        txtChacolateMuffin.configure(state=NORMAL)
        varChacolateMuffin.set("")
    elif(var13.get()==0):
        txtChacolateMuffin.configure(state=DISABLED)
        varChacolateMuffin.set("0")

def checkTea():
    if(var14.get()==1):
        txtTea.configure(state=NORMAL)
        varTea.set("")
    elif(var14.get()==0):
        txtTea.configure(state=DISABLED)
        varTea.set("0")

def checkCola():
    if(var15.get()==1):
        txtCola.configure(state=NORMAL)
        varCola.set("")
    elif(var15.get()==0):
        txtCola.configure(state=DISABLED)
        varCola.set("0")

def checkCoffee():
    if(var16.get()==1):
        txtCoffee.configure(state=NORMAL)
        varCoffee.set("")
    elif(var16.get()==0):
        txtCoffee.configure(state=DISABLED)
        varCoffee.set("0")

def checkWaterBottle():
    if(var17.get()==1):
        txtWaterBottle.configure(state=NORMAL)
        varWaterBottle.set("")
    elif(var17.get()==0):
        txtWaterBottle.configure(state=DISABLED)
        varWaterBottle.set("0")

def checkOrange():
    if(var18.get()==1):
        txtOrange.configure(state=NORMAL)
        varOrange.set("")
    elif(var18.get()==0):
        txtOrange.configure(state=DISABLED)
        varOrange.set("0")

def checkVanillaCone():
    if(var19.get()==1):
        txtVanillaCone.configure(state=NORMAL)
        varVanillaCone.set("")
    elif(var19.get()==0):
        txtVanillaCone.configure(state=DISABLED)
        varVanillaCone.set("0")

def checkVanillaShake():
    if(var20.get()==1):
        txtVanillaShake.configure(state=NORMAL)
        varVanillaShake.set("")
    elif(var20.get()==0):
        txtVanillaShake.configure(state=DISABLED)
        varVanillaShake.set("0")
def checkStrawberryShake():
    if(var21.get()==1):
        txtStrawberryShake.configure(state=NORMAL)
        varStrawberryShake.set("")
    elif(var21.get()==0):
        txtStrawberryShake.configure(state=DISABLED)
        varStrawberryShake.set("0")

def costofmeal():
    meal1=float(varFries.get())
    meal2=float(varSalad.get())
    meal3=float(varHamburger.get())
    meal4=float(varOnionrings.get())
    meal5=float(varChickensalad.get())
    meal6=float(varFishsandwich.get())
    meal7=float(varCheesesandwich.get())
    meal8=float(varChikensandwich.get())
 
    meal9=float(varHashBrown.get())
    meal10=float(varToastedBagel.get())
    meal11=float(varPancakesSyrup.get())
    meal12=float(varPineappleStick.get())
    meal13=float(varChacolateMuffin.get())
 
    meal14=float(varTea.get())
    meal15=float(varCola.get())
    meal16=float(varCoffee.get())
    meal17=float(varWaterBottle.get())
    meal18=float(varOrange.get())
    meal19=float(varVanillaCone.get())
    meal20=float(varVanillaShake.get())
    meal21=float(varStrawberryShake.get())


    iCost=((meal1*50)+(meal2*60)+(meal3*70)+(meal4*65)+(meal5*100)+(meal6*130)+(meal7*100)+(meal8*120)
                 +(meal9*150)+(meal10*200)+(meal11*250)+(meal12*200)+(meal13*180)+(meal14*10)+(meal15*50)
                 +(meal16*20)+(meal17*30)+(meal18*40)+(meal19*80)+(meal20*70)+(meal21*110))


    if(var22.get()=="Cash"):
        Change=float(varChange.get())
        Cost=((meal1*50)+(meal2*60)+(meal3*70)+(meal4*65)+(meal5*100)+(meal6*130)+(meal7*100)+(meal8*120)
                 +(meal9*150)+(meal10*200)+(meal11*250)+(meal12*200)+(meal13*180)+(meal14*10)+(meal15*50)
                 +(meal16*20)+(meal17*30)+(meal18*40)+(meal19*80)+(meal20*70)+(meal21*110))
        Tax=(Cost+3.4)/100
        Taxq="Rs",str('%.2f'%(Tax))
        varTax.set(Taxq)

        Costq="Rs",str('%.2f'%(Cost))
        varSubTotal.set(Costq)
        Total="Rs",str('%.2f'%((Cost+Tax)))
        varTotal.set(Total)

        Change=(Change-(Cost+Tax))
        Changeq="Rs",str('%.2f'%(Change))
        varChange.set(Changeq)
    elif(var22.get()=="Master Card" or "Visa Card" or "Debit Card" or "Credit Card" or "Internet Banking"):
        varChange.set("")
        Cost=((meal1*50)+(meal2*60)+(meal3*70)+(meal4*65)+(meal5*100)+(meal6*130)+(meal7*100)+(meal8*120)
                 +(meal9*150)+(meal10*200)+(meal11*250)+(meal12*200)+(meal13*180)+(meal14*10)+(meal15*50)
                 +(meal16*20)+(meal17*30)+(meal18*40)+(meal19*80)+(meal20*70)+(meal21*110))
        Tax=(Cost+3.4)/100
        Taxq="Rs",str('%.2f'%(Tax))
        varTax.set(Taxq)
        Costq="Rs",str('%.2f'%(Cost))
        varSubTotal.set(Costq)
        Totalq="Rs",str('%.2f'%((Cost+Tax)))
        varTotal.set(Totalq)
        varChange.set("")
     
     
     
     

#-------------------------FRAME-1-----------------------------------
lbmeal=Label(f1,font=('arial',18,'bold'),text="Fast Food Meal and vegitarian",fg='red')
lbmeal.grid(row=0,column=0)

Fries=Checkbutton(f1,text="Fries\t\tRs.50",variable=var1,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=checkFries).grid(row=1,column=0,sticky=W)
txtFries=Entry(f1,font=('arial',18,'bold'),textvariable=varFries,width=6,justify='right',state=DISABLED)
txtFries.grid(row=1,column=1)

Salad=Checkbutton(f1,text="Salad\t\tRs.60",variable=var2,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=checkSalad).grid(row=2,column=0,sticky=W)
txtSalad=Entry(f1,font=('arial',18,'bold'),textvariable=varSalad,width=6,justify='right',state=DISABLED)
txtSalad.grid(row=2,column=1)

Hamburger=Checkbutton(f1,text="Hamburger\tRs.70",variable=var3,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=checkHamburger).grid(row=3,column=0,sticky=W)
txtHamburger=Entry(f1,font=('arial',18,'bold'),textvariable=varHamburger,width=6,justify='right',state=DISABLED)
txtHamburger.grid(row=3,column=1)

Onionrings=Checkbutton(f1,text="Onionrings\tRs.65",variable=var4,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=checkOnionrings).grid(row=4,column=0,sticky=W)
txtOnionrings=Entry(f1,font=('arial',18,'bold'),textvariable=varOnionrings,width=6,justify='right',state=DISABLED)
txtOnionrings.grid(row=4,column=1)

Chickensalad=Checkbutton(f1,text="Chickensalad\tRs.100",variable=var5,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=checkChickensalad).grid(row=5,column=0,sticky=W)
txtChickensalad=Entry(f1,font=('arial',18,'bold'),textvariable=varChickensalad,width=6,justify='right',state=DISABLED)
txtChickensalad.grid(row=5,column=1)

lbsandwich=Label(f1,font=('arial',18,'bold'),text="Sandwich",fg='red')
lbsandwich.grid(row=6,column=0)

Fishsandwich=Checkbutton(f1,text="Fishsandwich\tRs.130",variable=var6,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=checkFishsandwich).grid(row=7,column=0,sticky=W)
txtFishsandwich=Entry(f1,font=('arial',18,'bold'),textvariable=varFishsandwich,width=6,justify='right',state=DISABLED)
txtFishsandwich.grid(row=7,column=1)

Cheesesandwich=Checkbutton(f1,text="Cheesesandwich\tRs.100",variable=var7,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=checkCheesesandwich).grid(row=8,column=0,sticky=W)
txtCheesesandwich=Entry(f1,font=('arial',18,'bold'),textvariable=varCheesesandwich,width=6,justify='right',state=DISABLED)
txtCheesesandwich.grid(row=8,column=1)

Chikensandwich=Checkbutton(f1,text="Chikensandwich\tRs.120",variable=var8,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=checkChikensandwich).grid(row=9,column=0,sticky=W)
txtChikensandwich=Entry(f1,font=('arial',18,'bold'),textvariable=varChikensandwich,width=6,justify='right',state=DISABLED)
txtChikensandwich.grid(row=9,column=1)

lbSpace=Label(f1,text="\n\n\n\n\n\n\n\n\n\n")
lbSpace.grid(row=10,column=0)


#----------------------------FRAME-2----------------------------------
lbmeal=Label(f2top,font=('arial',18,'bold'),text="Deserts",fg='red')
lbmeal.grid(row=0,column=0)

HashBrown=Checkbutton(f2top,text="HashBrown\tRs.150",variable=var9,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=checkHashBrown).grid(row=1,column=0,sticky=W)
txtHashBrown=Entry(f2top,font=('arial',18,'bold'),textvariable=varHashBrown,width=6,justify='right',state=DISABLED)
txtHashBrown.grid(row=1,column=1)

ToastedBagel=Checkbutton(f2top,text="ToastedBagel\tRs.200",variable=var10,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=checkToastedBagel).grid(row=2,column=0,sticky=W)
txtToastedBagel=Entry(f2top,font=('arial',18,'bold'),textvariable=varToastedBagel,width=6,justify='right',state=DISABLED)
txtToastedBagel.grid(row=2,column=1)

PancakesSyrup=Checkbutton(f2top,text="PancakesSyrup\tRs.250",variable=var11,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=checkPancakesSyrup).grid(row=3,column=0,sticky=W)
txtPancakesSyrup=Entry(f2top,font=('arial',18,'bold'),textvariable=varPancakesSyrup,width=6,justify='right',state=DISABLED)
txtPancakesSyrup.grid(row=3,column=1)

PineappleStick=Checkbutton(f2top,text="PineappleStick\tRs.200",variable=var12,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=checkPineappleStick).grid(row=4,column=0,sticky=W)
txtPineappleStick=Entry(f2top,font=('arial',18,'bold'),textvariable=varPineappleStick,width=6,justify='right',state=DISABLED)
txtPineappleStick.grid(row=4,column=1)

ChacolateMuffin=Checkbutton(f2top,text="ChacolateMuffin\tRs.180",variable=var13,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=checkChacolateMuffin).grid(row=5,column=0,sticky=W)
txtChacolateMuffin=Entry(f2top,font=('arial',18,'bold'),textvariable=varChacolateMuffin,width=6,justify='right',state=DISABLED)
txtChacolateMuffin.grid(row=5,column=1)


#-----------------------------------FRAME-3--------------------------

lbdrinks=Label(f3,font=('arial',18,'bold'),text="Drinks",fg='red')
lbdrinks.grid(row=0,column=0)

Tea=Checkbutton(f3,text="Tea\t\tRs.10",variable=var14,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=checkTea).grid(row=1,column=0,sticky=W)
txtTea=Entry(f3,font=('arial',18,'bold'),textvariable=varTea,width=6,justify='right',state=DISABLED)
txtTea.grid(row=1,column=1)

Cola=Checkbutton(f3,text="Cola\t\tRs.50",variable=var15,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=checkCola).grid(row=2,column=0,sticky=W)
txtCola=Entry(f3,font=('arial',18,'bold'),textvariable=varCola,width=6,justify='right',state=DISABLED)
txtCola.grid(row=2,column=1)

Coffee=Checkbutton(f3,text="Coffee\t\tRs.20",variable=var16,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=checkCoffee).grid(row=3,column=0,sticky=W)
txtCoffee=Entry(f3,font=('arial',18,'bold'),textvariable=varCoffee,width=6,justify='right',state=DISABLED)
txtCoffee.grid(row=3,column=1)

WaterBottle=Checkbutton(f3,text="WaterBottle\tRs.30",variable=var17,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=checkWaterBottle).grid(row=4,column=0,sticky=W)
txtWaterBottle=Entry(f3,font=('arial',18,'bold'),textvariable=varWaterBottle,width=6,justify='right',state=DISABLED)
txtWaterBottle.grid(row=4,column=1)

Orange=Checkbutton(f3,text="Orange\t\tRs.40",variable=var18,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=checkOrange).grid(row=5,column=0,sticky=W)
txtOrange=Entry(f3,font=('arial',18,'bold'),textvariable=varOrange,width=6,justify='right',state=DISABLED)
txtOrange.grid(row=5,column=1)

lbShakes=Label(f3,font=('arial',18,'bold'),text="Shakes",fg='red')
lbShakes.grid(row=6,column=0)

VanillaCone=Checkbutton(f3,text="VanillaCone\tRs.80",variable=var19,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=checkVanillaCone).grid(row=7,column=0,sticky=W)
txtVanillaCone=Entry(f3,font=('arial',18,'bold'),textvariable=varVanillaCone,width=6,justify='right',state=DISABLED)
txtVanillaCone.grid(row=7,column=1)

VanillaShake=Checkbutton(f3,text="VanillaShake\tRs.70",variable=var20,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=checkVanillaShake).grid(row=8,column=0,sticky=W)
txtVanillaShake=Entry(f3,font=('arial',18,'bold'),textvariable=varVanillaShake,width=6,justify='right',state=DISABLED)
txtVanillaShake.grid(row=8,column=1)

StrawberryShake=Checkbutton(f3,text="StrawberryShake\tRs.110",variable=var21,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=checkStrawberryShake).grid(row=9,column=0,sticky=W)
txtStrawberryShake=Entry(f3,font=('arial',18,'bold'),textvariable=varStrawberryShake,width=6,justify='right',state=DISABLED)
txtStrawberryShake.grid(row=9,column=1)

lbSpace=Label(f3,text="\n\n\n\n\n\n\n\n\n\n")
lbSpace.grid(row=10,column=0)

#-----------------------------------------------------------------------------------------------------------

lbPaymentMethod=Label(f2bottom,font=('arial',14,'bold'),text="Payment Method",bd=10,width=16,anchor='w')
lbPaymentMethod.grid(row=0,column=0)

lbChange=Label(f2bottom,font=('arial',14,'bold'),text="Change",bd=10,anchor='w')
lbChange.grid(row=0,column=1)
txtChange=Entry(f2bottom,font=('arial',14,'bold'),textvariable=varChange,width=6,state=DISABLED,justify='right')
txtChange.grid(row=0,column=2)

cmbPaymentMethod=ttk.Combobox(f2bottom,textvariable=var22,state="readonly",font=('arial',10,'bold'),width=20)
cmbPaymentMethod['value']=('Cash','Master Card','Visa Card','Debit Card','Credit Card','Internet Banking')
cmbPaymentMethod.current(0)
cmbPaymentMethod.grid(row=1,column=0)

lbTax=Label(f2bottom,font=('arial',14,'bold'),text="Tax",bd=10,anchor='w')
lbTax.grid(row=1,column=1)
txtTax=Entry(f2bottom,font=('arial',14,'bold'),textvariable=varTax,width=6,state=DISABLED,justify='right')
txtTax.grid(row=1,column=2)

txtPayment=Entry(f2bottom,font=('arial',18,'bold'),textvariable=varChange,width=6,state=DISABLED,justify='right')
txtPayment.grid(row=2,column=0)
lbSubTotal=Label(f2bottom,font=('arial',14,'bold'),text="SubTotal",bd=10,anchor='w')
lbSubTotal.grid(row=2,column=1)
txtSubTotal=Entry(f2bottom,font=('arial',14,'bold'),textvariable=varSubTotal,width=6,state=DISABLED,justify='right')
txtSubTotal.grid(row=2,column=2)

lbTotal=Label(f2bottom,font=('arial',14,'bold'),text="Total",bd=10,anchor='w')
lbTotal.grid(row=3,column=1)
txtTotal=Entry(f2bottom,font=('arial',14,'bold'),textvariable=varTotal,width=6,state=DISABLED,justify='right')
txtTotal.grid(row=3,column=2)
#---------------------------------------------

btnTotal=Button(f2bottom,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=5,text="Total",command=costofmeal).grid(row=4,column=0)

btnReSet=Button(f2bottom,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=5,text="ReSet",command=Reset).grid(row=4,column=1)

btnExit=Button(f2bottom,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=5,text="Exit",command=lambda:iExit()).grid(row=4,column=2)

lbSpace=Label(f2bottom,text="\n\n\n\n\n\n\n")
lbSpace.grid(row=5,column=0)
             
             

root.mainloop()
