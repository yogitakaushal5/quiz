#date=10/04/26
#assignment=2

#========================================
#        Assignment 1: Time Converter
#========================================
 
#Write a Python program that:
#- Accepts the total event duration in seconds as input.
#- Calculates how many hours, minutes, and seconds it corresponds to.
#- Displays the output in the format:
#  Hours: x, Minutes: y, Seconds: z

#Sample Input:
#Total event duration in seconds: 3672

#Sample Output:
#Hours: 1, Minutes: 1, Seconds: 12

"""
seconds=int(input("enter seconds:="))
hours=seconds//3600
minutes=(seconds%3600)//60
seconds=seconds%60
print("hours:=",hours," minutes:=",minutes," seconds:=",seconds)
"""



#========================================
#Assignment 2: Lifetime Calculator
#========================================
#You are developing a feature for a health and wellness mobile app
# that helps users understand how long they've been alive in a more tangible way.
#Write a Python program that:
#- Accepts the user’s age in years as input.
#- Calculates the approximate number of:
#  Days lived (1 year = 365 days)
#  Hours lived
#  Minutes lived
#- Displays the output in the format:
#You've lived approximately:
#Days: xxx
#Hours: yyy
#Minutes: zzz
#Sample Input:
#Enter your age in years: 18
#Sample Output:
#You've lived approximately:
#Days: 6570
#Hours: 157680
#Minutes: 9460800

"""

age=int(input("enter age:"))
days=age*365
hours=days*24
minutes=hours*60
print("you've lived approximately:")
print("days:=",days)
print("hours:=",hours)
print("minutes:=",minutes)
"""

#========================================
#Assignment 3: Split the Bill
#========================================

#You and your friends went out to eat. The bill was quite high and you want to split it evenly.

#Write a Python program that:
#- Accepts the total bill amount.
#- Accepts the number of friends.
#- Displays how much each person should pay.

#Example:
#Total bill = 1250
#Friends = 5
#Each should pay = 250.0



"""
total_bill=int(input("enter bill:="))
friends=int(input("enter friends:="))
each_pay=total_bill/friends
print("Each should pay =",each_pay)
"""


#========================================
#Assignment 4: Travel Fare Calculator
#========================================

#A cab company charges ₹15 per kilometer.

#Write a Python program that:
#- Accepts the number of kilometers traveled.
#- Calculates the total fare.
#- Displays the result.

#Example:
#Distance = 20 km
#Total fare = ₹300


"""
distance=float(input("enter distance:"))
fare=distance*15
print("total fare =",fare)
"""


"""
========================================
Assignment 5: Shopping Tax Calculator
========================================

Your shopping cart total doesn’t include tax. A 12% GST is applied.

Write a Python program that:
- Accepts the cart total amount.
- Calculates 12% tax.
- Displays the tax and final total amount.

Example:
Cart = ₹2000
Tax = ₹240
Total = ₹2240
"""


"""
cart=float(input("enter cart total amount:="))
tax=cart*0.12
total=cart+tax
print("tax:=",tax)
print("total:=",total)
"""

#========================================
#Assignment 6: Smart Coin Machine
#========================================

#You insert an amount into a vending machine. It returns coins using the largest denominations
 #possible (₹10 and ₹5).

#Write a Python program that:
#- Accepts the total amount.
#- Calculates how many ₹10 coins and ₹5 coins will be dispensed.
#- Displays the result.

#Example:
#Amount = ₹35
#Output = ₹10 x 3, ₹5 x 1


"""
amount=int(input("enter amount:"))
ten_coins=amount//10
remaining=amount%10
five_coins=remaining//5
print("10 coins",ten_coins, "5 coins",five_coins)
"""







#========================================
#Assignment 7: Temperature Converter
#========================================

#A weather application needs to convert temperature from Celsius to Fahrenheit.

#Write a Python program that:
#- Accepts temperature in Celsius as input.
#- Converts it to Fahrenheit using the formula:
#  F = (C × 9/5) + 32
#- Displays the result.

#Example:
#Celsius = 25
#Fahrenheit = 77.0

"""
c=float(input("enter celsius:"))
f=(c*9/5)+32
print("Fahrenheit :=",f)
"""

#========================================
#Assignment 8: Simple Interest Calculator
#========================================

#A bank wants to help customers calculate the simple interest on their savings.

#Write a Python program that:
#- Accepts principal amount, rate of interest, and time (in years) as input.
#- Calculates the simple interest using the formula:
#  SI = (P × R × T) / 100
#- Displays the simple interest.

#Example:
#Principal = 1000
#Rate = 5
#Time = 2
#Simple Interest = 100.0


p=float(input("enter principal:="))
r=float(input("enter rate:="))
t=float(input("enter time:="))
si=(p*r*t)/100
print("Simple Interest:=",si)

