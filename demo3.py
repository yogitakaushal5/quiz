#assignment-3
#date=11/04/26


"""
Assignment 1: Speed Calculator

Write a Python program that:

Accepts distance (in km) and time (in hours).
Calculates speed.

Input:
Distance = 120
Time = 2

Output:
Speed = 60 km/h 
"""

"""
distance=int(input("enter km"))
time=int(input("enter time"))
speed =distance/time
print("speed:=", speed)

"""

"""
Assignment 2: Salary Calculator

Write a Python program that:

Accepts daily wage and number of days.
Calculates total salary.

Input:
Daily wage = 500
Days = 26

Output:
Salary = 13000
"""
"""Salary Calculator"""

"""
daily_wage=int(input("enter daily wage:= "))
days=int(input("enter number of days:= "))
salary=daily_wage*days
print("Salary:=",salary)
"""

"""
Assignment 3: Electricity Bill Calculator

Write a Python program that:

Accepts number of units.
Calculates bill (₹6 per unit).

Input:
Units = 100

Output:
Bill = 600
"""

"""
units=int(input("enter number of units:= "))
bill=units*6
print("Bill:=", bill)
"""

"""
Assignment 4: Area of Rectangle

Write a Python program that:

Accepts length and breadth.
Calculates area.

Input:
Length = 10
Breadth = 5

Output:
Area = 50
"""
"""Area of Rectangle"""

"""
len=int(input("enter length:= "))
br=int(input("enter breadth:= "))

area=len*br

print("Area:=",area)
"""

"""
Assignment 5: Average Marks Calculator

Write a Python program that:

Accepts marks of 3 subjects.
Calculates average.

Input:
Marks = 80, 90, 70

Output:
Average = 80.0
"""
""" Average Marks Calculator"""

"""
m1=int(input("enter marks of subject 1:= "))
m2=int(input("enter marks of subject 2:= "))
m3=int(input("enter marks of subject 3:= "))
avg=(m1+m2+m3)/3
print("average:=", avg)
"""


"""
Assignment 6: Discount Calculator

Write a Python program that:

Accepts total amount.
Calculates 10% discount and final price.

Input:
Amount = 1000

Output:
Discount = 100
Final = 900
"""
"""Discount Calculator"""


"""
amt=int(input("enter total amount:= "))

dis=amt*0.10
final_price=amt-dis

print("discount :=", dis)
print("Final:=", final_price)
"""

"""
Assignment 7: Circle Area Calculator

Write a Python program that:

Accepts radius.
Calculates area of circle.

Input:
Radius = 7

Output:
Area = 153.86
"""
""" Circle Area Calculator """

"""
r=float(input("enter radius:= "))
area=3.14*r*r
print("Area:=",round(area,2))
"""

"""
Assignment 8: Data Storage Converter

Write a Python program that:

Accepts value in MB.
Converts into GB.

Input:
MB = 2048

Output:
GB = 2.0
"""
"""
mb=float(input("enter MB: "))
gb=mb/1024
print("GB:=",gb)
"""

"""
Assignment 9: Fuel Cost Calculator

Write a Python program that:

Accepts distance (km), mileage (km/litre), and petrol price.
Calculates total fuel cost.

Input:
Distance = 100
Mileage = 20
Petrol Price = 100

Output:
Cost = 500
"""

"""
d=float(input("enter distance: "))
m=float(input("enter mileage: "))
p=float(input("enter petrol price: "))

cost=(d/m)*p
print("Cost :=",cost)
"""

"""
Assignment 10: Percentage Calculator

Write a Python program that:

Accepts total marks and obtained marks.
Calculates percentage.

Input:
Total = 500
Obtained = 400

Output:
Percentage = 80%
"""

"""

t=float(input("enter total marks:= "))
o=float(input("enter obtained marks: "))

per=(o/t)*100
print("Percentage:=",per)
"""

"""
Assignment 11: Time Duration Adder

Write a Python program that:

Accepts hours, minutes, seconds.
Converts into total seconds.

Input:
Hours = 1
Minutes = 2
Seconds = 30

Output:
Total Seconds = 3750
"""
"""
h=int(input("enter hours:= "))
m=int(input("enter minutes:= "))
s=int(input("enter seconds:= "))

total=h*3600+m*60+s
print("total seconds:=",total)
"""


"""
Assignment 12: Change Return System

Write a Python program that:

Accepts amount.
Calculates ₹100, ₹50, ₹10 notes.

Input:
Amount = 380

Output:
₹100 x 3
₹50 x 1
₹10 x 3
"""

"""
amt=int(input("enter amount:= "))

n100=amt//100
n50=(amt%100)//50
n10=(amt%50)//10

print("100 x",n100)
print("50 x",n50)
print("10 x",n10)
"""

"""
Assignment 13: Compound Interest Calculator

Write a Python program that:

Accepts principal, rate, and time.
Calculates compound interest.

Input:
Principal = 1000
Rate = 10
Time = 2

Output:
Amount = 1210.0
Compound Interest = 210.0
"""

"""
p=float(input("enter principal:= "))
r=float(input("enter rate:= "))
t=float(input("enter time:= "))

a=p*(1+r/100)**t
ci=a-p

print("amount:=",a)
print("compound interest:=",ci)
"""

"""
Assignment 14: Simple Profit or Loss Calculator

Write a Python program that:

Accepts cost price and selling price.
Calculates profit/loss and percentage.

Input:
Cost Price = 1000
Selling Price = 1200

Output:
Profit = 200
Profit % = 20.0
"""
"""
cp=float(input("enter cost price: "))
sp=float(input("enter selling price: "))

if sp>cp:
    profit=sp-cp
    per=(profit/cp)*100
    print("profit:=",profit)
    print("profit % :=",per)
else:
    loss=cp-sp
    per=(loss/cp)*100
    print("loss:=",loss)
    print("loss%:=",per)
    
"""    

"""
Assignment 15: Average Speed for Multiple Trips

Write a Python program that:

Accepts distance1, time1, distance2, time2.
Calculates average speed.

Input:
Distance1 = 60
Time1 = 1
Distance2 = 40
Time2 = 1

Output:
Average Speed = 50 km/h
"""

d1=float(input("enter distance1:= "))
t1=float(input("enter time1:= "))
d2=float(input("enter distance2:= "))
t2=float(input("enter time2:= "))

total_d=d1+d2
total_t=t1+t2

avg=total_d/total_t
print("average speed:=",avg)
