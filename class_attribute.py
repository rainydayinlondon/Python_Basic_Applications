# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 17:15:50 2021

@author: Feyza
"""


class User:
    active_users=0   #Class attribute
    
    def __init__(self,first,last,age):
        self.first=first
        self.last=last
        self.age=age
        User.active_users+=1
        
    def full_name(self):
        return f"{self.first} {self.last}"
    
    def logout(self):
        User.active_users=User.active_users-1
        return f"{self.full_name()} uygulamadan çıkış yaptı"

print(User.active_users)
UserA=User("Feyza","Ç",29)
UserB=User("Ayşe","A",30)
print(User.active_users)


print(UserA.full_name())
print(UserB.full_name())


print(UserA.logout())