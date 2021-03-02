# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 14:07:17 2021

@author: Feyza
"""

f=open("msg.txt")
print(f)  #<_io.TextIOWrapper name='msg.txt' mode='r' encoding='cp1254'>

# print(help(f))  # dökümantasyonunu incelemek istersek...


print(f.read())  # Dosyayı okumak için


f.seek(0)  #Cursor'u en başa almış olduk..

f.close()

print(f.closed)   #KAPALI MI DOSYAAA

