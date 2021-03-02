# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 14:35:15 2021

@author: Feyza
"""


try:
    with open("msg.txt","r",encoding="utf-8") as file:
         for i in file:
              print(i, end="")
except FileNotFoundError as e:
    print("dosya okuma hatası :",e)


finally:
    print("Dosya Kapandı..")