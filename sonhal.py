# Kütüphaneler Eklenecek Burada
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from pandastable import Table, TableModel
from skimage import data, color
from skimage.transform import rescale, resize, downscale_local_mean
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os
import cv2
import glob
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

#global değişkenler
data = ""
dataUzunluk =""
siGramDegerleri=[]
kGramDegerleri =[]
alGramDegerleri=[]
tiGramDegerleri=[]
feGramDegerleri=[]
mnGramDegerleri=[]
mgGramDegerleri=[]
caGramDegerleri=[]
naGramDegerleri=[]
pGramDegerleri =[]


"""BİLİMSEL İŞLEMLER"""

class Hesaplamalar () :
    def Si(data):
        global siGramDegerleri
        print("Toplam Eleman Sayımız:", dataUzunluk)
        if ornekSec.get()=="":
            for a in data["SiO2"].values :           
                siGram= a/60*1000
                siGramDegerleri.append(siGram)
                print("Gerekli İşlem Sonunda Sırasıyla Si Değerlerimiz",siGram)
        else:
            siGram= data["SiO2"].values[int(ornekSec.get())]/60*1000 
            siGramDegerleri=siGram
        return siGramDegerleri

    def K (data):
        global kGramDegerleri
        print("Toplam Eleman Sayımız:", dataUzunluk)
        if ornekSec.get()=="":
            for b in data["K2O"].values :
                kGram=b/47*1000
                kGramDegerleri.append(kGram)
                print("Gerekli İşlem Sonunda Sırasıyla K Değerlerimiz", kGram)
        else:
            kGram=data["K2O"].values[int(ornekSec.get())]/47*1000
            kGramDegerleri=kGram
        return kGramDegerleri
    
    def Al (data):
        global alGramDegerleri
        print("Toplam Eleman Sayımız:", dataUzunluk)
        if ornekSec.get()=="":
            for c in data["Al2O3"].values :
                alGram=c/51*1000
                alGramDegerleri.append(alGram)
                print("Gerekli İşlem Sonunda Sırasıyla Al Değerlerimiz" , alGram)
        else:
            alGram=data["Al2O3"].values[int(ornekSec.get())]/51*1000
            alGramDegerleri=alGram                
        return alGramDegerleri
            
    def Ti (data): 
        global tiGramDegerleri
        print("Toplam Eleman Sayımız:", dataUzunluk)
        if ornekSec.get()=="":
            for d in data["TiO2"].values :
                tiGram=d/80*1000
                tiGramDegerleri.append(tiGram) 
                print("Gerekli İşlem Sonunda Sırasıyla Ti Değerlerimiz",tiGram )
        else:
            tiGram=data["TiO2"].values[int(ornekSec.get())]/80*1000
            tiGramDegerleri=tiGram
        return tiGramDegerleri
    
    def Fe (data):
        global feGramDegerleri
        print("Toplam Eleman Sayımız:", dataUzunluk)
        if ornekSec.get()=="":
            for e in data["Fe2O3"].values :
                feGram=e/80*1000
                feGramDegerleri.append(feGram) 
                print("Gerekli İşlem Sonunda Sırasıyla Fe Değerlerimiz" , feGram)
        else:
            feGram=data["Fe2O3"].values[int(ornekSec.get())]/80*1000
            feGramDegerleri=feGram
        return feGramDegerleri
    
    def Mn (data) :
        global mnGramDegerleri
        print("Toplam Eleman Sayımız:", dataUzunluk)
        if ornekSec.get()=="":
            for f in data["MnO"].values :
                mnGram=f/71*1000
                mnGramDegerleri.append(mnGram) 
                print("Gerekli İşlem Sonunda Sırasıyla Mg Değerlerimiz" , mnGram)
        else:
            mnGram=data["MnO"].values[int(ornekSec.get())]/71*1000
            mnGramDegerleri=mnGram
        return mnGramDegerleri
    
    def Mg (data) :
        global mgGramDegerleri
        print("Toplam Eleman Sayımız:", dataUzunluk)
        if ornekSec.get()=="":
            for g in data["MgO"].values :
                mgGram=g/40*1000
                mgGramDegerleri.append(mgGram) 
                print("Gerekli İşlem Sonunda Sırasıyla Mg Değerlerimiz" , mgGram)
        else:
            mgGram=data["MgO"].values[int(ornekSec.get())]/40*1000
            mgGramDegerleri=mgGram
        return mgGramDegerleri
    
    def Ca (data):
        global caGramDegerleri 
        print("Toplam Eleman Sayımız:", dataUzunluk)
        if ornekSec.get()=="":
            for h in data["CaO"].values :
                caGram=h/56*1000
                caGramDegerleri.append(caGram) 
                print("Gerekli İşlem Sonunda Sırasıyla Ca Değerlerimiz" , caGram)
        else: 
            caGram=data["CaO"].values[int(ornekSec.get())]/56*1000
            caGramDegerleri=caGram
        return caGramDegerleri
    
    def Na (data):
        global naGramDegerleri 
        print("Toplam Eleman Sayımız:", dataUzunluk)
        if ornekSec.get()=="":
            for ı in data["Na2O"].values :
                naGram=ı/31*1000
                naGramDegerleri.append(naGram) 
                print("Gerekli İşlem Sonunda Sırasıyla Na Değerlerimiz" , naGram)
        else:
            naGram=data["Na2O"].values[int(ornekSec.get())]/31*1000
            naGramDegerleri=naGram
        return naGramDegerleri
    
    def P (data):
        global pGramDegerleri 
        print("Toplam Eleman Sayımız:", dataUzunluk)
        if ornekSec.get()=="":
            for i in data["P2O5"].values :
                pGram=i/71*1000
                pGramDegerleri.append(pGram) 
                print("Gerekli İşlem Sonunda Sırasıyla P Değerlerimiz" , pGram)
        else:
            pGram=data["P2O5"].values[int(ornekSec.get())]/71*1000
            pGramDegerleri=pGram
        return pGramDegerleri
    
class qpGrafik():
    def qpXEkseni(data):
        global siGramDegerleri,kGramDegerleri,naGramDegerleri,caGramDegerleri
        Hesaplamalar.Si(data)
        Hesaplamalar.Ca(data)
        Hesaplamalar.K(data)
        Hesaplamalar.Na(data)
        xEkseni=[] # K-(Na+Ca)
        if ornekSec.get()=="":
            for i in range (len(data)):
                xEkseniHesaplama = kGramDegerleri[i]-(naGramDegerleri[i]+caGramDegerleri[i])
                xEkseni.append(xEkseniHesaplama)
        else:
            xEkseniHesaplama = kGramDegerleri-(naGramDegerleri+caGramDegerleri)
            xEkseni=xEkseniHesaplama
        return xEkseni
    
    def qpYEkseni(data):
         global kGramDegerleri,naGramDegerleri,caGramDegerleri
         Hesaplamalar.Ca(data)
         Hesaplamalar.K(data)
         Hesaplamalar.Na(data)
         yEkseni=[] # Si/3-(K+Na+2Ca/3)  
         if ornekSec.get()=="":
             for i in range (len(data)):
                 yEkseniHesaplama= siGramDegerleri[i]/3 - (kGramDegerleri[i]+naGramDegerleri[i]+2*caGramDegerleri[i]/3)
                 yEkseni.append(yEkseniHesaplama)
         else:
             yEkseniHesaplama= siGramDegerleri/3 - (kGramDegerleri+naGramDegerleri+2*caGramDegerleri/3)
             yEkseni=yEkseniHesaplama
         return yEkseni 
        
class baGrafik():
    def baXEkseni(data):
        global feGramDegerleri,mgGramDegerleri,tiGramDegerleri
        Hesaplamalar.Fe(data)
        Hesaplamalar.Mg(data)
        Hesaplamalar.Ti(data)
        xEkseni=[] # B = Fe+Mg+Ti
        if ornekSec.get()=="":
            for i in range (len(data)):
                xEkseniHesaplama = feGramDegerleri[i]+ mgGramDegerleri[i]+tiGramDegerleri[i]
                xEkseni.append(xEkseniHesaplama)
        else:
            xEkseniHesaplama = feGramDegerleri+ mgGramDegerleri+tiGramDegerleri
            xEkseni=xEkseniHesaplama
        return xEkseni
    
    def baYEkseni(data):
        global alGramDegerleri,kGramDegerleri,naGramDegerleri,caGramDegerleri
        Hesaplamalar.Al(data)
        Hesaplamalar.Ca(data)
        Hesaplamalar.K(data)
        Hesaplamalar.Na(data)
        yEkseni=[] # A= Al-(K+Na+2Ca)
        if ornekSec.get()=="":
            for i in range (len(data)):
                yEkseniHesaplama = alGramDegerleri[i]-(kGramDegerleri[i]+naGramDegerleri[i]+2*caGramDegerleri[i])
                yEkseni.append(yEkseniHesaplama)
        else:
            yEkseniHesaplama = alGramDegerleri-(kGramDegerleri+naGramDegerleri+2*caGramDegerleri)
            yEkseni=yEkseniHesaplama
        return yEkseni
    
class r1r2Grafik():
    def r1r2XEkseni(data):
        global siGramDegerleri,naGramDegerleri,kGramDegerleri,feGramDegerleri,tiGramDegerleri
        Hesaplamalar.Si(data)
        Hesaplamalar.Na(data)
        Hesaplamalar.K(data)
        Hesaplamalar.Fe(data)
        Hesaplamalar.Ti(data)
        xEkseni=[] # R1 = 4Si-11(Na+K)-2(Fe+Ti)
        if ornekSec.get()=="":
            for i in range(len(data)):
                xEkseniHesaplama = 4*siGramDegerleri[i]-11*(naGramDegerleri[i]+kGramDegerleri[i])-2*(feGramDegerleri[i]+tiGramDegerleri[i])
                xEkseni.append(xEkseniHesaplama)
        else:
            xEkseniHesaplama = 4*siGramDegerleri-11*(naGramDegerleri+kGramDegerleri)-2*(feGramDegerleri+tiGramDegerleri)
            xEkseni=xEkseniHesaplama       
        return xEkseni                    
    def r1r2YEkseni(data):
        global caGramDegerleri,mgGramDegerleri, alGramDegerleri
        Hesaplamalar.Ca(data)
        Hesaplamalar.Mg(data)
        Hesaplamalar.Al(data)
        yEkseni=[] # R2= 6Ca+2Mg+Al
        if ornekSec.get()=="":
            for i in range(len(data)):
                yEkseniHesaplama= 6*caGramDegerleri[i]+2*mgGramDegerleri[i]+alGramDegerleri[i]
                yEkseni.append(yEkseniHesaplama)
        else:
            yEkseniHesaplama= 6*caGramDegerleri+2*mgGramDegerleri+alGramDegerleri
            yEkseni=yEkseniHesaplama 
        return yEkseni

canvas=""
class Görsellestirme():
    def qpGörsel(data):
        global canvas
        x=qpGrafik.qpXEkseni(data)
        y=qpGrafik.qpYEkseni(data)
        img = plt.imread("QPGraph.png")
        if canvas=="":
            fig, ax = plt.subplots()
            ax.imshow(img,zorder=0,extent=[-400,120,0,270])
            plt.xlabel("P= K-(Na+Ca)")
            plt.ylabel("Q=Si/3-(K+Na+2Ca/3)")
            plt.title("Debon and Le Fort (QP) Diyagram")
            ax.plot(x,y,".",linewidth=1, color="blue") 
            canvas = FigureCanvasTkAgg(fig, master=labelGrafik)     
            canvas.get_tk_widget().pack(side="top", fill="both", expand=1)
            canvas._tkcanvas.pack(side="top", fill="both", expand=1) 
        elif canvas !="":
            canvas.get_tk_widget().destroy()
            fig, ax = plt.subplots()
            ax.imshow(img,zorder=0,extent=[-400,120,0,270])
            plt.xlabel("P= K-(Na+Ca)")
            plt.ylabel("Q=Si/3-(K+Na+2Ca/3)")
            plt.title("Debon and Le Fort (QP) Diyagram")
            ax.plot(x,y,".",linewidth=1, color="blue") 
            canvas = FigureCanvasTkAgg(fig, master=labelGrafik)     
            canvas.get_tk_widget().pack(side="top", fill="both", expand=1)
            canvas._tkcanvas.pack(side="top", fill="both", expand=1)              
        return ax.plot(x,y,".",linewidth=5, color="blue")
     
    def baGörsel(data):
        global canvas
        x=baGrafik.baXEkseni(data)
        y=baGrafik.baYEkseni(data)
        img=plt.imread("BAGraph.png")
        if canvas=="":
            fig, ax = plt.subplots()
            ax.imshow(img,zorder=0,extent=[0,500,-500,500])
            plt.xlabel("B= Fe+Mg+Ti")
            plt.ylabel("A=Al-(K+Na+2Ca)")
            plt.title("Debon and Le Fort (BA) Diyagram")
            ax.plot(x,y,".",linewidth=5, color="red")   
            canvas = FigureCanvasTkAgg(fig, master=labelGrafik)     
            canvas.get_tk_widget().pack(side="top", fill="both", expand=1)
            canvas._tkcanvas.pack(side="top", fill="both", expand=1)
        elif canvas !="":
            canvas.get_tk_widget().destroy()
            fig, ax = plt.subplots()
            ax.imshow(img,zorder=0,extent=[0,500,-500,500])
            plt.xlabel("B= Fe+Mg+Ti")
            plt.ylabel("A=Al-(K+Na+2Ca)")
            plt.title("Debon and Le Fort (BA) Diyagram")
            ax.plot(x,y,".",linewidth=5, color="red")   
            canvas = FigureCanvasTkAgg(fig, master=labelGrafik)     
            canvas.get_tk_widget().pack(side="top", fill="both", expand=1)
            canvas._tkcanvas.pack(side="top", fill="both", expand=1)          
        return ax.plot(x,y,".",linewidth=5, color="red")
    
    def r1r2Görsel(data):
        global canvas
        x=r1r2Grafik.r1r2XEkseni(data)
        y=r1r2Grafik.r1r2YEkseni(data)
        img = plt.imread("R1R2Graph.png")
        if canvas=="":
            fig, ax = plt.subplots()
            ax.imshow(img,zorder=0,extent=[-1000,4000,0,4000])
            plt.xlabel("R1= 4Si- 11(Na+K)- 2(Fe+Ti")
            plt.ylabel("R2= 6Ca+ 2Mg+ Al")
            plt.title("Granitoyidlerin Jeotektonik Ortamları (Batchelor & Bowden, 1989) R1-R2 Grafiği")
            ax.plot(x,y,".",linewidth=5, color="blue")
            canvas = FigureCanvasTkAgg(fig, master=labelGrafik)     
            canvas.get_tk_widget().pack(side="top", fill="both", expand=1)
            canvas._tkcanvas.pack(side="top", fill="both", expand=1)
        elif canvas !="":
            canvas.get_tk_widget().destroy()
            fig, ax = plt.subplots()
            ax.imshow(img,zorder=0,extent=[-1000,4000,0,4000])
            plt.xlabel("R1= 4Si- 11(Na+K)- 2(Fe+Ti")
            plt.ylabel("R2= 6Ca+ 2Mg+ Al")
            plt.title("Granitoyidlerin Jeotektonik Ortamları (Batchelor & Bowden, 1989) R1-R2 Grafiği")
            ax.plot(x,y,".",linewidth=5, color="blue")
            canvas = FigureCanvasTkAgg(fig, master=labelGrafik)     
            canvas.get_tk_widget().pack(side="top", fill="both", expand=1)
            canvas._tkcanvas.pack(side="top", fill="both", expand=1)           
        return ax.plot(x,y,".",linewidth=5, color="red")


"""Ana Penceremizi Burada Oluşturuyoruz"""
window = tk.Tk()
window.geometry("1600x650") # burada arayüzümüzün boyutlarını belirliyoruz.
window.wm_title("Proje") # burada penceremize isim veriyoruz

# Frameleri hazırlıyoruz
frame1= tk.Frame(window, width = 1600, height = 100 ) #Buton ve seçenekler bölümü
frame1.grid(row=0, column=0, columnspan=2)

frame2 = tk.Frame(window, width=950, height=550 ) #Grafik görselleştirme bölümü
frame2.grid (row=1, column=0 )

frame3 = tk.Frame(window, width = 650, height = 550) #Bilgiler bölümü
frame3.grid(row=1, column=1)

#Ana frameler üzerine label frameleri ekliyoruz
labelSecenek = tk.LabelFrame (frame1, width= 1590, height = 96)
labelSecenek.grid(row=0, column=0,columnspan=2, padx=5, pady=2) 

labelGorsellestirme = tk.LabelFrame(frame2,  width =950, height =546)
labelGorsellestirme.pack(fill=tk.BOTH, expand=1)

labelGrafik = tk.LabelFrame(frame3, width = 640, height = 546)
labelGrafik.grid(row=1, column=1 , padx=5, pady=2)      

         
def dataAc():
    global data, dataUzunluk #bu fonksiyonun içinde global data ve data uzunluk bilgilerini alacağız
    dataYolu=filedialog.askopenfilename(filetypes = [("All files", "*.*")] )
    data = pd.read_excel(dataYolu) # datayı alıyoruz
    dataUzunluk =len(data) # data uzunluk bilgisini alıyoruz        
    df=data
    pt = Table(labelGorsellestirme, dataframe=df, showtoolbar=True, showstatusbar=True, width=800, height=400)
    pt.show()

# Burada grafik çiz butonunu çalıştırıyoruz
def grafikCiz(): 

    if diyagramSec.get()=="Debon and Le Fort (QP)":
        Görsellestirme.qpGörsel(data)           
    elif diyagramSec.get()== "Debon and Le Fort (BA)":
        Görsellestirme.baGörsel(data)
    elif diyagramSec.get()== "Batchelor & Bowden, 1989 R1-R2":
        Görsellestirme.r1r2Görsel(data)

""" Anapenceremizin İçini Doldurmaya Başlıyoruz"""
# Frame1 için;
dataAcButon = tk.Button(labelSecenek, text="Data Seç", command=dataAc, width=15)
dataAcButon.place(relx = 0.02,  rely = 0.3) 

başlatButon = tk.Button(labelSecenek, text="Grafik Çiz", command=grafikCiz, width=15)
başlatButon.place(relx = 0.85,  rely = 0.27) 

tk.Label(labelSecenek, text="Örnek Seçiniz:", font="Times 11").place(relx = 0.2,  rely = 0.3) 
ornekSec = tk.Entry(labelSecenek, width =5 , bd =2)
ornekSec.place(relx = 0.33,  rely = 0.3) 

tk.Label(labelSecenek, text="Diyagram Seçiniz:", font="Times 11").place(relx = 0.42,  rely = 0.3) 
diyagramAdi = tk.StringVar() 
diyagramSec = ttk.Combobox(labelSecenek, width = 25, textvariable = diyagramAdi)
diyagramSec['values'] = ("Debon and Le Fort (QP)", "Debon and Le Fort (BA)" , "Batchelor & Bowden, 1989 R1-R2")
diyagramSec.place(relx = 0.58,  rely = 0.3) 
diyagramSec.current()




window.mainloop() 