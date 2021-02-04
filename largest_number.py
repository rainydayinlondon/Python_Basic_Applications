# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 13:31:32 2021

@author: Feyza
"""

# Python program to find largest 
# number in a list 
def high_and_low(numbers):
    
    max = numbers[0] 
    min =numbers[0]
    
    for i in numbers:
        if i>max:
            max=i
        
        if i<min:
            min=i
  
    return max,min

numbers=[1364,6,2,9,3]

print("Largest element and min number:", high_and_low(numbers)) 
