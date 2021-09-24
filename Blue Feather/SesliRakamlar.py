from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox 
import random as rnd
from functools import partial
import pygame

"""Pencere"""
form2=tk.Toplevel()
form2.configure(bg="#f9e5bc")
form2.title("Sesli Rakamlar")
form2.geometry("800x600+400+100")
form2.resizable(False,False)


sayac=0
"""Kullanıcıya Dinletilen Ses"""
def dinle(button_id):
    button_id=1
    global sayac
    global seviye
    sayac+=1                                
    dinlebtn.config(state=DISABLED)        
    rndsayi=rnd.randint(0,9)              
    pygame.mixer_music.load("sesler\\"+str(rndsayi)+".mp3") 
    pygame.mixer_music.play(loops=0)     
    sayilar.append(rndsayi)             
    sayilarkopya.append(rndsayi)          
        
    """Secilen Zorluk Seviyesine Göre Çalma Hızı ve Çalma Sayısı"""
    if sayac!=4 and seviye==1:              
        dinlebtn.after(1500,dinle,1)    #1,5 Saniyede Bir Ses Çalıyor 4 Kere
    if sayac!=5 and seviye==2:
        dinlebtn.after(1000,dinle,2)    #1 Saniyede Bir Ses Çalıyor 5 kere
    if sayac!=6 and seviye==3:
        dinlebtn.after(750,dinle,3)     #0,75Ms'de Bir Ses Çalıyor 6 Kere

    if sayac==seviye+3:                    
        for i in range(seviye+3):
            suffle=rnd.choice(sayilarkopya) #Sayılar Kopya listesinden Rastgele değer seçiliyor
                                            #değer buttonun üzerine yazılıyor
            sayibtn.append(Button(form2,border=3,text=suffle,font=("Helvetica", 20),command=partial(yaz, i)))
            Rakamlist.append(suffle)           
            sayilarkopya.remove(suffle)     
        sayac=0
        form2.after(1000,buttonlaridiz)     #Üzerinde Rakam Yazan Butonları Getir

    """Dinle Butonu Tanımlaması"""
bg=ImageTk.PhotoImage(Image.open("images\\dinle.jpg"))
dinlebtn=tk.Button(form2,text="Dinle",command=partial(dinle,1),font=("Helvetica", 20),border=0,image=bg)

"""Zorluk Seçimi Butonlarının Ekrandan Silinmesi Dinle Butonunun Ekrana Yerleştirilmesi"""
def zorluk(button_id):
    global seviye
    seviye=button_id
    print("zorluk seviyesi "+str(seviye))
    Kolay.place_forget()       
    Orta.place_forget()        
    Zor.place_forget()       
                                
    dinlebtn.place(width=100,height=100,x=form2.winfo_screenwidth()/4-35,y=form2.winfo_screenheight()/4)
    lbl.config(text="Dinlediğiniz Rakamları Aklınızda Tutun")
seviye=0

"""Zorluk Seçimi Button Tanımlaması"""

Kolay=tk.Button(form2,text="Kolay",command=partial(zorluk, 1),font=("Helvetica", 20),border=0)
Kolay.place(width=150,height=75,x=form2.winfo_screenwidth()/4-35,y=form2.winfo_screenheight()/4-75)

Orta=tk.Button(form2,text="Orta",command=partial(zorluk, 2),font=("Helvetica", 20),border=0)
Orta.place(width=150,height=75,x=form2.winfo_screenwidth()/4-35,y=form2.winfo_screenheight()/4+50)

Zor=tk.Button(form2,text="Zor",command=partial(zorluk, 3),font=("Helvetica", 20),border=0)
Zor.place(width=150,height=75,x=form2.winfo_screenwidth()/4-35,y=form2.winfo_screenheight()/4+175)

"""Buttonların Yerleşimi"""
def buttonlaridiz():
    global seviye
    global x
    global y
    if seviye==1:
        x=215
    if seviye==2:
        x=165
    if seviye==3:
        x=115
    for i in range(seviye+3):
        sayibtn[i].place(width=75,height=75,x=x,y=y)
        x+=100

    
    tbox.place(width=150,height=25,x=400,y=y-50,anchor="center")    
    tbox.focus_set()                                                
    pasgecbtn.place(width=175,height=50,x=315,y=y+100)             
    silbtn.place(width=75,height=75,x=615+((seviye-1)*50),y=y)     
    dinlebtn.place_forget()                                        

    """Metin kutusuna tıklanan butonunun değerinin girilmesi ve sorgulanması"""
RakamSirasi=""
def yaz(button_id):
    global RakamSirasi
    tbox.insert("end",Rakamlist[button_id])                        
    inputValue=tbox.get("1.0","end-1c")                            
    RakamSirasi=""                                        
    for i in range(seviye+3):   
        RakamSirasi+=str(sayilar[i])                
    print(RakamSirasi)
    print(sayilar)
    if inputValue==RakamSirasi:                             
        print("next question")
        pas()                                               

    """Pas Geç Butonunun Fonksiyonu"""
def pas():                      
    global seviye
    global RakamSirasi
    tbox.delete("1.0","end")                          
    tbox.place_forget()                               
    pasgecbtn.place_forget()                      
    silbtn.place_forget()                         
                                            
    dinlebtn.place(width=100,height=100,x=form2.winfo_screenwidth()/4-35,y=form2.winfo_screenheight()/4)
    for i in range(seviye+3):
        sayibtn[i].place_forget()                   
    sayibtn.clear()                                  
    sayilar.clear()                                           
    Rakamlist.clear()                                            
    dinlebtn.config(state=ACTIVE)                        
    RakamSirasi=""                                           
    return RakamSirasi                                              

    """Sil Butonunun Fonksiyonu"""
def sil():
    tbox.delete(1.0,END)                                           
    tbox.focus_set()                                       


pygame.mixer.init()         #Program içinde Seslerin Çalabilmesi için Kullanılan metod
x=215
y=400
sayilar=[]
sayilarkopya=[]
Rakamlist=[]
sayibtn=[]

"""Metin kutusu - Sil,Pas butonu tanımlaması"""
pasgecbtn=tk.Button(form2,text="Pas geç",command=lambda: pas(),font=("Helvetica", 20),border=0)
silbtn=tk.Button(form2,text="Sil",command=lambda: sil(),font=("Helvetica", 20),border=0)
tbox=Text(form2)

lbl=Label(form2,text="Zorluk Seç",font=("Helvetica", 20),bg="#f9e5bc")
lbl.place(x=form2.winfo_screenwidth()/4+35,y=form2.winfo_screenheight()/8-50,anchor="center")

form2.mainloop()