# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 10:01:18 2021

@author: Feyza
"""

# 1- Kullanıcıdan aldığı ürün bilgisini (ad, fiyat) urunler.txt dosyasına kayıt eden fonksiyon.



# def urun_ekle(ad,fiyat):
#      with open("urunEkle.txt",'a') as file:
#          file.write(f"ad: {ad},fiyat:{fiyat}\n")
        
 

# urun_ekle("samsung s10", 5000)
# urun_ekle("iphone s10", 10000)
# # urun_ekle("samsung s11", 6000)

# # 2- dosya ismi, eski kelime ve yeni kelime parametrelerini alarak dosyada bir güncelleme
# # yapan fonksiyon.


def bul_degistir(dosya_ismi,eski_kelime,yeni_kelime):
    with open(dosya_ismi,"r+")as file:
        text=file.read()
        yeni_text=text.replace(eski_kelime,yeni_kelime)
        file.seek(0)
        file.write(yeni_text)
        file.truncate()
        

bul_degistir("urunEkle.txt","10000","12000")






