#date =14/04/26
#assignment=4

"""
Assignment 1: Restaurant Bill Split

A group of friends went to a restaurant. The restaurant adds GST and service charge to the
 bill, and then the total is divided equally.

Input:
Total bill amount = 2500
GST = 5%
Service charge = 10%
Number of friends = 4

Expected Output:
Final Bill = 2875.0
Each Person Pays = 718.75
"""
"""
total_bill=2500
gst=total_bill*0.05
sc=total_bill*0.1
friends=4
final_bill=total_bill+gst+sc
each_person=final_bill/friends

print("final bill:=",final_bill)
print("each person pays:=", each_person)
"""



"""
Assignment 2: Mobile EMI Calculation

You purchased a mobile phone using EMI. After paying a down payment, the remaining amount 
includes interest and is divided into monthly installments.

Input:
Mobile price = 30000
Down payment = 5000
Interest rate = 10%
Months = 10

Expected Output:
Remaining Amount = 25000
Total with Interest = 27500
Monthly EMI = 2750.0
"""

"""
mobile_price=30000
down_payment=5000
interest_rate=10
months=10

remaining_amount=mobile_price-down_payment
interest=(interest_rate/100)*remaining_amount
total_with_interest=remaining_amount+interest
monthly_emi=total_with_interest/months

print("remaining amount:=",remaining_amount)
print("total with interest:=", total_with_interest)
print("monthly EMI:=", monthly_emi)
"""


"""
Assignment 3: Student Marks Analysis

A student wants to calculate total marks, average, and percentage from 5 subjects.

Input:
Marks = 78, 85, 90, 88, 80

Expected Output:
Total = 421
Average = 84.2
Percentage = 84.2
"""

"""
m1=78
m2=85
m3=90
m4=88
m5=80

total=m1+m2+m3+m4+m5
average=total/5
percentage=total/500*100
print("Total =", total)
print("Average =", average)
print("Percentage =", percentage)
"""

"""
Assignment 4: Travel Distance Calculation

A person is traveling at a constant speed. Time is given in hours and minutes. Convert total time into hours and calculate distance.

Input:
Speed = 60 km/hr
Time = 2 hours 30 minutes

Expected Output:
Total Time = 2.5 hours
Distance = 150.0 km
"""
"""
speed=60
hours=2
minutes=30

total_time=hours+(minutes/60)
distance=speed*total_time
print("total time:=",total_time,"hours")
print("Distance:=",distance,"km")
"""

"""
Assignment 5: Salary Breakdown

An employee wants to calculate salary per day and per hour.

Input:
Monthly salary = 36000
Working days = 24
Working hours per day = 8

Expected Output:
Salary per day = 1500.0
Salary per hour = 187.5
"""
"""
monthly_salary=36000
working_days=24
hours_per_day = 8

salary_per_day=monthly_salary/working_days

salary_per_hour=salary_per_day/hours_per_day

print("salary per day:=", salary_per_day)
print("salary per hour:=", salary_per_hour)

"""
"""
Assignment 6: Data Storage Conversion

A user wants to convert data from GB into MB and KB.

Input:
Data = 5 GB

Expected Output:
In MB = 5120.0
In KB = 5242880.0
"""

data_gb=5

mb=data_gb*1024
kb=mb*1024
print("in MB:=", mb)
print("in KB:=", kb)


"""
Assignment 7: Cricket Run Rate

In cricket, overs are given in decimal format (e.g., 48.3 means 48 overs and 3 balls). Convert overs into total balls and calculate run rate.

Input:
Total runs = 275
Overs = 48.3

Expected Output:
Total Balls = 291
Run Rate = 5.67
"""

"""
runs = 275
overs = 48.3
total_balls = 48 * 6 + 3
run_rate = runs / (total_balls / 6)

print("Total Balls =", total_balls)
print("Run Rate =", round(run_rate, 2))
"""
"""
Assignment 8: Compound Interest

A person invests money in a bank that provides compound interest annually.

Input:
Principal = 10000
Rate = 5%
Time = 2 years

Expected Output:
Amount after interest = 11025.0
"""
"""
principal = 10000
rate = 5
time = 2

# Compound Interest Formula
amount = principal * (1 + rate/100) ** time

print("Amount after interest =", amount)
"""

"""
Assignment 9: Petrol Cost Calculation

You traveled a certain distance. Based on mileage and petrol price, calculate fuel used and total cost.

Input:
Distance = 450 km
Mileage = 15 km/litre
Petrol price = 110/litre

Expected Output:
Petrol Used = 30.0 litres
Total Cost = 3300.0
"""
"""
used=450/15
cost=used*110

print("Petrol Used =",used,"litres")
print("Total Cost =",cost)
"""
"""
Assignment 10: Time Conversion

Convert total seconds into hours, minutes, and seconds.

Input:
Total seconds = 7384

Expected Output:
Hours = 2
Minutes = 3
Seconds = 4
"""
"""
h=7384//3600
rem=7384%3600
m=rem//60
s=rem%60

print("Hours =",h)
print("Minutes =",m)
print("Seconds =",s)
"""
"""
Assignment 11: Expression Evaluation

A billing system applies nested calculations with discounts and extra charges using brackets and unary operators.

Input:
50 + (10 * (+(2**3))) / 4 - (-6 % 4)
"""

"""
result=50+(10*(+(2**3)))/4-(-6%4)
print(result)
"""

"""
Assignment 12: Expression Evaluation

A gaming score system calculates bonus points using exponent and applies penalties using unary negative values and brackets.

Input:
100 - (20 * (3**2)) + (40 / (+5)) - (-3)
"""

"""
result=100-(20*(3**2))+(40/(+5))-(-3)
print(result)
"""

"""
Assignment 13: Expression Evaluation

A shopping application applies offers using exponent and grouped calculations with unary adjustments.

Input:
25 + (5 * (6**2) // 3) - (-(8 % 5)) + (+2)
"""
"""
result=25+(5*(6**2)//3)-(-(8%5))+(+2)
print(result)
"""
"""
Assignment 14: Expression Evaluation

A travel fare calculator computes total fare using grouped operations, power calculations, and unary adjustments.

Input:
(80 / (4 * 2)) * (+(2**2)) + 15 - (-(9 % 2))
"""

"""
result=(80/(4*2))*(+(2**2))+15-(-(9%2))
print(result)
"""

"""
Assignment 15: Expression Evaluation

An electricity billing system uses nested brackets, exponent-based scaling, and unary corrections.

Input:
60 + (12 * (2**3) // (+(4))) - (-(10 % 3))
"""


"""
result=60+(12*(2**3)//(+(4)))-(-(10%3))
print(result)
"""




"""
Assignment 16: Expression Evaluation

A performance evaluation system calculates final score using grouped operations, exponent, division, and unary adjustments.

Input:
45 + (15 * (2**2)) - (20 / (+(5))) + (-(7 % 3))
"""

"""
result=45+(15*(2**2))-(20/(+5))+(-(7%3))
print(result)
"""
