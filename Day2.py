# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 10:48:57 2019

@author: STEM
"""
#example code from nasrine
def cadburyBox(box):
    cadburyBox = box + 10
    print(cadburyBox)
cadburyBox(5)

#my code
cadburyBox = 15
cadburyBox = cadburyBox + 5
print(cadburyBox)

#code for chocolate in the box
cadbury1 = "Milk Chocolate"
cadbury2 = "Dark Chocolate"
cadbury3 = "White Chocolate"
print("There is", cadbury1, "," , cadbury2, ", and" , cadbury3, "in the box")

#another version of code for chocolate with the def function
def cadburyBox(w,d,m):
    print("There is", m, "," , d, ", and" , w, "in the box") 
cadburyBox("White Chocolate", "Dark Chocolate", "Milk Chocolate")

#function to greet a person
def greeting(name):
    print("Hello", name)
greeting("Ashlyn")

#input function to greet a person
name = input("Please enter your name: ")
print("Hello", name)

#input function to get a person's age
age = input("Enter your age: ")
print("Your age is", age)
ageInt = float(age)
ageInt

#import the math library
import math
dir(math)
math.factorial(1)
math.pi
math.pow(5/6,4/15)

#a function that produces the cubic root of a number
def cubeRoot(num):
    print("The cubic root of the", num, "is", math.pow(num, 1/3))
cubeRoot(8)


num = input("Enter a number for the cubic root: ")
num = int(num)
print("The cubic root of", num, "is", math.pow(num, 1/3))





