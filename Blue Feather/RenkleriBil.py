import tkinter
import tkinter as tk
import random
from tkinter import messagebox
                                                            #Türkçe Giriş İçin Renkler
colourName = ['Kırmızı','Mavi','Yeşil','Pembe','Siyah',
        'Sarı','Turuncu','Beyaz','Mor','Kahverengi']
                                                            #Yazıların Rengi
colours = ['Red','Blue','Green','Pink','Black',
        'Yellow','Orange','White','Purple','SaddleBrown']        

global kalanSure
global skor
global i
skor = 0
i=0
kalanSure = 30

def oyun(event):        
    if kalanSure == 30:     
        sayac()
    sıradakiRenk()

    """Metin kutusundaki değerin karşılaştırılması ve yeni değer üretilmesini sağlayan metod"""
def sıradakiRenk(): 
    global i
    global skor 
    global kalanSure 
    
    if kalanSure > 0:   
        tBox.focus_set()                                            
        if tBox.get().lower() == colourName[i].lower():          
            skor += 1 
        tBox.delete(0, tkinter.END)                                
        rndRenk=random.choice(colours)                             
        rndRenkIndex=colours.index(rndRenk)                        
        i=rndRenkIndex                                              
        rndYazi=random.choice(colourName)                           
        yaziLabel.config(fg = str(rndRenk), text = str(rndYazi))   
        skorLabel.config(text = "Skor: " + str(skor))               
    if kalanSure==0:
        ExitApplication()                                           #Süre 0 a ulaşınca Çıkış veya Tekrar oyna seçeneği sunan method
            
    """30 dan geriye sayan sayac metodu"""
def sayac():
    global kalanSure
    global skor 
    if kalanSure > 0:                       
        kalanSure -= 1
        sureLabel.config(text = "Kalan Süre: "+ str(kalanSure))     #Ekranda Gözüken Süre
        sureLabel.after(1000, sayac)                               

"""Form Pencere Bilgileri"""
form1 = tkinter.Toplevel() 
form1.title("Renk Oyunu") 
form1.geometry("430x200+600+300") 

"""Buttonlar ve Label'lar"""
    
aciklama = tkinter.Label(form1, text = "Kelime metnini değil, kelimelerin rengini yazın!", font = ('Helvetica', 12)) 
aciklama.pack()  
    
skorLabel = tkinter.Label(form1, text = "Başlamak için tıklayın", font = ('Helvetica', 12)) 
skorLabel.pack() 
    
sureLabel = tkinter.Label(form1, text = "Kalan Süre: " +str(kalanSure), font = ('Helvetica', 12)) 
sureLabel.pack() 
    
# Ekranda görülen yazıların bulunduğu etiket
yaziLabel = tkinter.Label(form1, font = ('Helvetica', 60,'bold')) 
yaziLabel.pack() 
    
# Girdi yapmak için metin kutusu
tBox = tkinter.Entry(form1) 
tBox.pack() 

"""Pencere içerisinde fare ile sol tık veya enter tuşuna basılınca sıradaki rengi geçiş yapan 'oyun' fonksiyonunu calıştıran yer"""
form1.bind("<Return>", oyun)    #enter'a basılınca
form1.bind('<Button -1>', oyun) #fare sol tık'a basılınca  
tBox.focus_set()               

"""Süre Bitince Çalışan Fonksiyon"""
def ExitApplication():   
    global skor
    global kalanSure
    #Skor hakkında bilgi ve Tekrar oynamak isteyip istemediğinizi soran uyarı mesajı kısmı
    MsgBox = tk.messagebox.askquestion ("Süre Bitti Skor : "+str(skor),"Tekrar oynamak ister misin ?",icon = 'warning')
    if MsgBox == 'yes':      
        kalanSure=30          
        skor=0                  
        skorLabel.config(text="Başlamak için tıklayın")
    else:                     
        form1.destroy()         #formu kapat
    
"""Form kapatılmak istendiğinde"""
def CloseForm():
    MsgBox = tk.messagebox.askquestion ("Oyundan Çık","Çıkmak İstediğinizden Emin Misiniz?",icon = 'warning')
    if MsgBox == 'yes':
        form1.destroy()         #oyun ekranını kapat


form1.protocol("WM_DELETE_WINDOW", CloseForm) 

    
form1.mainloop() #form'un açık kalması için gereken metod