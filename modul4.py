import os
import math
os.system('cls')
"""
längd=int(input("Skirv din längd "))

if längd < 150:
    print("Du får tyvär inte åka denna atraktion ")
elif längd >= 150:
    print("Grattis! du får åka denna atraktion ")

name=input("Vad heter du? ")
print(f"Hej och välkommen {name}!")

while True:
    try:
        int(input("Hur gammal är du? "))
        break 
    except:
        print("Skriv siffror tack :) ")

while True:
    try:
        Weight=int(input ("Din vikt ")) #Bmi kalkylator 
        break
    except:
        print("Bara siffror tack! ")

while True:
    try:
        Height=int(input ("Din längd "))
        break
    except:
        print("Bara siffror tack!")

Height=Height/100
print ("din bmi är ", Weight / (Height ** 2))

pi=math.pi

while True:
    try:
        r=float(input("Skriv in radien "))
        break
    except: 
        print("Bara siffror tack!")

Area=r*r*pi
print(round(Area))
"""
while True:
    calc=input("(+) (-) (*) (/) eller S för att avsluta ")
    if calc in("+","-","*","/"):
       pass 
    elif calc==("S"):
       break
    elif calc==("s"):
       break
    else:
      print("skriv rätt tecken")
    
    if calc== ("+"):
     while True:
        try: 
            a=float(input("tal 1 "))
            break
        except:
           print("skriv rätt tecken")

        
     while True:    
        try:
            b=float(input("tal 2 "))
            break
        except:
            print("skriv rätt tecken")
     print ("svaret är", a + b)
    
    if calc==("-"):
     while True:
        try:
            c=float(input("tal 1 "))
            break
        except:
           print("skriv rätt tecken")
     
     while True:
        try:
            d=float(input("tal 2 "))
            break
        except:
           print("skriv rätt tecken")
     print ("svaret är",c - d)

    if calc==("*"):
     while True:
        try:
            e=float(input("tal 1 "))
            break
        except:
            print("skriv rätt tecken")
       
     while True:
        try:
            f=float(input("tal 2 "))
            break
        except:
            print("skriv rätt tecken")
     print("svaret är", e * f)


    if calc==("/"):
     while True:
        try:
            g=float(input("tal 1 "))
            break
        except:
            print("skriv rätt tecken")
     while True:
        try:
            h=float(input("tal 2 "))
            if h == 0:
                print("Du får inte dividera med noll")
            else:
               break
        except:
            print("Skriv rätt tecken")
     print("svaret är",g / h)