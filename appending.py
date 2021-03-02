# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 17:55:00 2021

@author: Feyza
"""

# open(dosya_adi,dosya_erişim_modu)
# dosya_erişim_modu => dosyayı hangi amaçla açtığımızı belirtir.

# "r": (Read) okuma. Dosya konumda yoksa hata verir.
# "w": (Write) yazma modu. 
#    ** Dosyayı konumda oluşturur. 
#    ** Dosya içeriğini siler ve yeniden ekleme yapar. 
# "a": (Append) ekleme. Dosya konumda yoksa oluşturur.
# "r+": Hem okuma hem yazma modunda açılır. Dosya konumda yoksa hata verir.

# with open("msg.txt","a") as file:
#     file.write("dördüncü satır\n")
#     file.write("beşinci satır\n")





# with open("msg.txt","a",encoding="UTF-8") as file:  # Bilgi eklemek istersek...
#       file.write("\ndördüncü satır\n")
#       file.write("\nbesinci satır\n")
      
      
      

# with open("msg.txt","a",encoding="UTF-8") as file:  # Dosya sonunu bilgi eklemek istersek...
#       file.seek(0)
#       file.write("\nyeni satır\n")

      

      

with open("msg.txt","r+") as file:  # Dosya başına eklemek istersek...
      
      file.write("yeni mısra\n")
    

      
      
      