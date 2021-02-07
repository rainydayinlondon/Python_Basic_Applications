# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 16:02:56 2021

@author: Feyza
"""


class Person:
    #Yapıcı Methotlar
    def __init__(self,name,surname,year):
        
        #Object attributes
        self.name=name
        self.surname=surname
        self.year=year
        
    def intro(self):
        return f"Benim adım {self.name} ve soyadım {self.surname}"
        
    def calculate_age(self):
        return f"Ve yaşım iseee {2021-self.year}"

        
p1=Person("Feyza","Çerezci",1991)

print(p1.intro())  #Intro nedir ? Kaç kelimedirrr ??


print(p1.calculate_age())