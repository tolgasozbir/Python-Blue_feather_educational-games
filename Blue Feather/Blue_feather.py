import tkinter as tk
from PIL import Image, ImageTk
from time import strftime               #Sistem Saati

def elementlerOyunu():
    import Elementler

def sesliRakamlarOyunu():
    import SesliRakamlar

def renkleriBilOyunu():
    import RenkleriBil

"""Pencere Başlığında Gözüken Saatin Fonksiyonu"""
def saat():                         
    string = strftime('%H:%M:%S')      
    form.title("Blue Feather "+string) 
    form.after(1000, saat)             


#pencere
form=tk.Tk()
form.title("Blue Feather")
form.resizable(False,False)
form.geometry("800x600+400+100")

#background pic--------------Arkaplanda Bulunan Hareketli Resim----------

gif=[]                     
for i in range(120):       
    gif.append(ImageTk.PhotoImage(Image.open("main\\"+"gif ("+str(i)+").jpg")))

gifnum=0
def bgGif():
    global gifnum
    lblbg.config(image=gif[gifnum])    
    gifnum+=1                           
    lblbg.after(50,bgGif)               

    if gifnum==120:                   
        gifnum=0

#-----------------------------------------------------------------------


"""Oyun Buttonlarının Tanımlanması, Yerleştirilmesi ve Resimlerinin Adresi"""

lblbg=tk.Label(form,)
lblbg.pack()
bgGif()                
saat()                  

elementlerBg=ImageTk.PhotoImage(Image.open("images\\element.jpg"))
renklerbg=ImageTk.PhotoImage(Image.open("images\\colour.jpg"))
sesliRakamlarBg=ImageTk.PhotoImage(Image.open("images\\sesliRakamlar.jpg"))

ElementOyun=tk.Button(form,text="",image=elementlerBg,border=0,bg="white",command=elementlerOyunu)
ElementOyun.place(width=75,height=75,x=form.winfo_screenwidth()/4-125,y=form.winfo_screenheight()/4+250)

RenkOyun=tk.Button(form,text="",image=renklerbg,command=renkleriBilOyunu)
RenkOyun.place(width=75,height=75,x=form.winfo_screenwidth()/4+125,y=form.winfo_screenheight()/4+250)

SesliRakamOyun=tk.Button(form,text="",image=sesliRakamlarBg,command=sesliRakamlarOyunu)
SesliRakamOyun.place(width=75,height=75,x=form.winfo_screenwidth()/4,y=form.winfo_screenheight()/4+250)

form.mainloop()