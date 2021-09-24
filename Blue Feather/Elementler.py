from tkinter import *
import tkinter as tk
from tkinter import messagebox 
from PIL import Image, ImageTk
import random as rnd
from functools import partial
import pygame
import Elements #Soruların Geldiği py Dosyası

"""Pencere Tanımlaması ve Boyutu Ayarları"""
form=tk.Toplevel()
form.configure(bg="#dddddd")
form.title("Elementler")
form.resizable(False,False)
form.state("zoomed")

"""Buttonlar için Resim Array'i"""
images=[]
for i in range(120):
    images.append(ImageTk.PhotoImage(Image.open("element\\"+str(i)+".png")))
soruNo=0

"""Element Tablosundaki Buttonların Tıklanma Olayı"""
def btnclick(button_id):                 
    print(button_id)
    global soruNo
    Splay()                              
    HarfBtnTemizle()                      
    soruNo=button_id                      
    sorulabel.configure(text=Elements.ElementsInfo.elementsInfoList[soruNo]) 
    cevapList=[]                       
    cevapList.clear()                      
    harfButton.clear()                      
    HarfListesi.clear()                    
    cevapList=list(Elements.ElementsInfo.cevap[soruNo])           #Sorunun Cevabının diziye alınması örnek ['K', 'R', 'O', 'M'] olarak
    uzunlukCevapList=len(cevapList)         
    harfButtonx=form.winfo_screenwidth()/2  #Harf buttonlarının x konumunda ekranın ortasının koordinatını alıyorum
    harfButtony=780                         #Harf buttonlarının y konumunda yerleşiceği y koordinatını veriyorum
    x=True

    """Harf Buttonlarının Tanımlanması ve Dizilimi"""
    for i in range(uzunlukCevapList):       
        harf=rnd.choice(cevapList)          #Cevap string listesinden rastgele harf alıyor

        harfButton.append(Button(form,border=3,text=harf,font=("Helvetica", 20),command=partial(harfBtn, i)))
        
        """Harf Buttonlarının Dizilimi"""
        if uzunlukCevapList%2==0 and x==True:
            harfButtonx-=40
            x=False
        harfButton[i].place(width=60,height=60,x=harfButtonx,y=harfButtony,anchor="center")
        HarfListesi.append(harf)        #harflistesine rastgele alınan harfin eklenmesi
        cevapList.remove(harf)          #eklenen harfin tekrar eklenmemesi için listeden çıkarılması

        """ Harf Buttonların x ekseninde dizilimi ortada olması için bir sağına bir soluna eklenerek gidiyor"""
        if uzunlukCevapList%2==1:
            if i==0:
                harfButtonx+=75
            elif i==1:
                harfButtonx-=150
            elif i==2:
                harfButtonx+=225
            elif i==3:
                harfButtonx-=300
            elif i==4:
                harfButtonx+=375
            elif i==5:
                harfButtonx-=450
            elif i==6:
                harfButtonx+=525
            elif i==7:
                harfButtonx-=600
            elif i==8:
                harfButtonx+=675
            elif i==9:
                harfButtonx-=750
            elif i==10:
                harfButtonx+=825
        if uzunlukCevapList%2==0:
            if i==0:
                harfButtonx+=75
            elif i==1:
                harfButtonx-=150
            elif i==2:
                harfButtonx+=225
            elif i==3:
                harfButtonx-=300
            elif i==4:
                harfButtonx+=375
            elif i==5:
                harfButtonx-=450
            elif i==6:
                harfButtonx+=525
            elif i==7:
                harfButtonx-=600
            elif i==8:
                harfButtonx+=675
            elif i==9:
                harfButtonx-=750
            elif i==10:
                harfButtonx+=825

    return soruNo                    

"""Element Tablosunun Buttonlarının Array Üzerinden Oluşturulması ve Yerleşimi"""
x=225                           # X ekseninde button koordinatı
y=10                            # Y ekseninde button koordinatı

buttons = []                    # Element Buttonlarının Dizisi
for i in range(0,120):
                                #Buttonların listeye eklenmesi, id verilmesi ve click metodu
    buttons.append(Button(form,border=0,image=images[i],command=partial(btnclick, i)))
    buttons[i].place(x=x,y=y)   #Butonun x ve y koordinatına yerleştirilmesi
    x+=60
    if i==0:
        x+=960
    elif i==1:
        x=225
        y=70
    elif i==3:
        x+=600
    elif i==9:
        x=225
        y=130
    elif i==11:
        x+=600
    elif i==17:
        x=225
        y=190
    elif i==35:
        x=225
        y=250
    elif i==53:
        x=225
        y=310
    elif i==71:
        x=225
        y=370
    elif i==89:
        x=405
        y=460
    elif i==104:
        x=405
        y=520
    print(i)

"""Harf Buttonlarını Temizleme fonksiyonu"""
def HarfBtnTemizle():
        for elemans in harfButton:
            elemans.place_forget()

harfButton=[]                               #Harf Buttonlarının tutulduğu liste      
Puan=0

"Bilinen bir kullanımı olmayan elementlerin kapatılması işlemi butonlar deaktif hale getiriliyor"
for sil in range(74,90):
    buttons[sil].config(state=DISABLED)
buttons[56].config(state=DISABLED)



HarfListesi=[]                               #Cevap harflerinin tutulduğu liste

"""Harf Buttonuna Tıklanma Olayı"""
def harfBtn(button_id):
    hrf=HarfListesi[button_id]              
    print(hrf)
    tbox.insert("end",hrf)                  


"""Joker Butonu Hover Özelliği ve Durum Çubuğu Tanımlaması"""
def button_hover(e):                                                    
    status_label.config(text="Kalan Joker Hakkınız "+str(Joker))        
def button_hover_leave(e):                                              
    status_label.config(text="")                                        
status_label=Label(form,text="Alt bilgi",bd=1,relief=SUNKEN, anchor=E)  
status_label.pack(fill=X, side=BOTTOM, ipady=2)                         

"""Joker Hakkı Button, Button Resimi ve Fonskiyonu"""
Joker=3                                                                 
images.append(ImageTk.PhotoImage(Image.open("images\\jokzilla.png")))  
                                                                       
jokerbtn=tk.Button(form,text="Joker\n"+str(Joker),command=lambda: using_joker(),font=("Helvetica", 20),border=0,image=images[120],bg="#dddddd",activebackground="#dddddd")
jokerbtn.place(width=170,height=170,x=1325,y=15)                       
jokerbtn.bind("<Enter>",button_hover)                               
jokerbtn.bind("<Leave>",button_hover_leave)                            

"""Joker Fonksiyonu Tıklandığında Sorunun Cevabını TextBox'a Girme İşlemi"""
def using_joker():
    global Joker
    inputValue=tbox.get("1.0","end-1c")                               
    if (Joker>0) and (inputValue!=Elements.ElementsInfo.cevap[soruNo]):
        tbox.delete("1.0","end")                                       
        tbox.insert("1.0",Elements.ElementsInfo.cevap[soruNo])         
        Joker-=1                                                       



streak=-1                                                              
jokerkazan=0  

"""TextBox'a Girilen Girdinin Kontrolü"""
def retrieve_input():
    global soruNo
    global Puan
    global streak
    global jokerkazan
    global Joker
    inputValue=tbox.get("1.0","end-1c")         #Metin kutusuna girilen değerin değişkene atanması
    print(inputValue)

    """Girilen Değer Doğruysa Yapılacak İşlemler"""
    if  str.upper(inputValue)==Elements.ElementsInfo.cevap[soruNo]:    
        Cplay()                                
        streak+=1                               
        jokerkazan+=1                           #Joker kazanmak için sayaç
        if jokerkazan==10 :                     #Joker sayacı 10 olduğunda 1 adet joker hakkı ekliyor
            Joker+=1                            
            jokerkazan=0                        
            sorulabel.configure(text="Doğru Cevap 1 Joker hakkı kazandınız")
        else:
            sorulabel.configure(text="Doğru Cevap")
        Puan+=100+(streak*10)                   #puan sistemi
        lblPuan.configure(text=Puan)           
        tbox.delete("1.0","end")                
        buttons[soruNo].config(state=DISABLED)  
        tbox.focus_set()                        

        """Harf Butonlarının ekrandan silinmesi işlemi"""
        HarfBtnTemizle()
        
        """Girilen Değer Yanlış İse Yapılacak İşlemler"""
    else:
        Wplay()                                 #Yanlış Cevap Sesi
        Puan-=30                                
        lblPuan.configure(text=Puan)            
        streak=-1                               

"""Button - Label - Textbox Tanımlaması ve Konumlandırılması"""

lblSuperAgırElementler=Label(form,text="Süperağır Elementler. Radyoaktiftirler, doğada doğal olarak bulunamazlar, Atomik araştırmalar dışında kullanılmazlar.",font=("Helvetica", 10),bg="#dddddd")
lblSuperAgırElementler.place(x=800,y=440,anchor="center")

tbox=Text(form)                                                         #Cevapların girildiği metin kutusu
tbox.place(width=120,height=25,x=form.winfo_screenwidth()/2,y=form.winfo_screenheight()/2+260,anchor="center")

btn=tk.Button(form,text="Yanıtla",command=lambda: retrieve_input())     #Yanıtla butonu
btn.place(width=120,height=25,x=form.winfo_screenwidth()/2,y=form.winfo_screenheight()/2+300,anchor="center")

                        #soruların ekranda gözüktüğü label
sorulabel=Label(form,text="Başlamak İçin Element Seçin",font=("ComicSans", 14),fg="#b36b00",bg="#dddddd")
sorulabel.place(x=form.winfo_screenwidth()/2,y=form.winfo_screenheight()/2+200,anchor="center")

                        #Lantanitler ve Aktinitler yazılı label'lar
lblLantanitler=Label(form,text="Lantanitler",font=("Helvetica", 20),bg="#dddddd")
lblLantanitler.place(x=250,y=475)
lblAktinitler=Label(form,text="Aktinitler",font=("Helvetica", 20),bg="#dddddd")
lblAktinitler.place(x=250,y=525)

                        #Puanın yazılıdığı label
lblPuantext=Label(form,text="Puan",font=("Helvetica", 25),bg="#dddddd")
lblPuantext.place(x=500,y=40,anchor="center")
lblPuan=Label(form,text=Puan,font=("Helvetica", 25),bg="#dddddd")
lblPuan.place(x=500,y=90,anchor="center")

"""Kronometre"""
Second=00
Minute=00
def tick():
    global Second
    global Minute
    Second+=1

    if Second<10:
        mylabel.configure(text="Geçen Süre\n"+ str(Minute)+ " : 0" +str(Second))
    elif Second==60:
        Second=0
        Minute+=1
    
    if Minute<10:
        mylabel.configure(text="Geçen Süre\n0"+ str(Minute)+ " : " +str(Second))

    if Second<10 and Minute<10:
        mylabel.configure(text="Geçen Süre\n0"+ str(Minute)+ " : 0" +str(Second))

    if Second>=10 and Minute>=10:
        mylabel.configure(text="Geçen Süre\n"+ str(Minute)+ " : " +str(Second))

    mylabel.after(1000,tick)        #Recursive fonksiyon her 1 saniyede kendisini çağırıyor

mylabel=Label(form,text="xx:xx")    #gecen sürenin gözüktüğü label
mylabel.pack()

tick()


"""Oyunda Bulunan Seslerin Fonksiyonları"""
pygame.mixer.init()

def Wplay():            #Cevap Yanlış ise
    pygame.mixer_music.load("sesler\\Swrong.wav")
    pygame.mixer_music.play(loops=0)

def Cplay():            #Cevap Doğru ise
    pygame.mixer_music.load("sesler\\SCorrect.wav")
    pygame.mixer_music.play(loops=0)

def Splay():            #Element Butonlarına tıklanınca çalıcak olan sesler
    rndsoru=rnd.randint(0,2)
    if rndsoru==0:
        pygame.mixer_music.load("sesler\\SSoru1.mp3")
        pygame.mixer_music.play(loops=0)
    elif rndsoru==1:
        pygame.mixer_music.load("sesler\\SSoru2.wav")
        pygame.mixer_music.play(loops=0)
    else:
        pygame.mixer_music.load("sesler\\SSoru3.wav")
        pygame.mixer_music.play(loops=0)


form.mainloop()     #Formun açık kalmasını sağlayan fonksiyon