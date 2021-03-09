# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 19:00:50 2021

@author: Feyza
"""


def dosya_kopyala(dosya_ismi,yeni_dosya_ismi):
    with open(dosya_ismi,"r") as file:
        data=file.read()

    with open(yeni_dosya_ismi,"w") as file2:
        file2.write(data)
        
dosya_kopyala("msg.txt","msgkopyas.txt")
        

#Dosya_kopyala fonksiyonunu işlevsel hale getiriniz.


def ters_cevir(dosya_ismi,yeni_dosya_ismi):
    with open(dosya_ismi,"r") as file:
         data=file.read()  
         
        
    with open(yeni_dosya_ismi,"w") as file2:
        file2.write(data[::-1])
        
        
ters_cevir("msg.txt","msg_ters.txt")    
    

#Eski dosyadaki tüm içerikleri yeni dosyaya tersten yazdırınız..


     
        
     
def bilgilendir(dosya_ismi):
    with open(dosya_ismi) as file:
        satirlar = file.readlines()

    sonuc = {
        "satir_sayisi": len(satirlar),
        "kelime_sayisi": sum(len(satir.split(' ')) for satir in satirlar),
        "karakter_sayisi": sum(len(satir) for satir in satirlar)
    }
    return sonuc
    


# def bilgilendir(dosya_ismi):
#      with open(dosya_ismi) as file:
#           satirlar=file.readlines()
         
#      sonuc = {
#          "satir_sayisi": len(satirlar),
#          "kelime_sayisi":sum(len(satir.split(' ')) for satir in satirlar),
#          "karakter_sayisi":sum(len(satir) for satir in satirlar)
         
         
#          }
         
#      return sonuc
 
    
 
def bilgilendir(dosya_ismi):
    with open(dosya_ismi) as file:
        satirlar = file.readlines()

    sonuc = {
        "satir_sayisi": len(satirlar),
        "kelime_sayisi": sum(len(satir.split(' ')) for satir in satirlar),
        "karakter_sayisi": sum(len(satir) for satir in satirlar)
    }
    return sonuc

print(bilgilendir("msg.txt"))

        



#Fonksiyona gönderilen dosya içindeki verilerin özet bilgisini hazırlayınız.
#{"satir_sayisi:52" ,"kelime_sayisi":158,"karakter_sayisi":1250}

