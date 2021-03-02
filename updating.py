# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 18:21:27 2021

@author: Feyza
Bu eğitim dersinde, listenin en aşağı kısmına append komutu ile değil de , istediğimiz
kısmına ekleme yapmamızı sağlayan kodlar bulunuyor...

"""




# with open("markalar.txt","a") as file:  # append  - dosyanın sonuna append işlemi yapmış oluyoruz..
#      file.write("6-BMW")




# with open("markalar.txt","r+",encoding="utf-8")as file:
#     markalar=file.read()
#     markalar="1-Toyota\n"+markalar
#     print(markalar)
#     file.seek(0)
#     file.write(markalar)
    


with open("markalar.txt","r+",encoding="utf-8")as file:
    markalar=file.readlines()  #Satır satır okumamızı sağlıyor..
    markalar.insert(2,"3-Renault\n")
    file.seek(0)
    # for marka in markalar:
    #     file.write(marka)  #ekrana yazdırdık..
    file.writelines(markalar)  # Dizinin elemanlarını tek tek yazdır..
    





with open("markalar.txt") as file:
    print(file.read())   # markalar txt dosyasını açmış olduk...
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    