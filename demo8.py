#date 20/04/26
#assignment=8


"""
1. Electricity Department Billing System

The electricity department of a city wants to automate the monthly bill generation process for its customers. The bill is calculated based on slab-wise unit consumption:

First 100 units are charged at *5 per unit

Next 100 units (101-200) are charged at 7 per unit

Units above 200 are charged at *10 per unit

Write a Python program to calculate the total electricity bill based on the number of units consumed.

Input:

Enter units consumed: 250

Output:

Total Electricity Bill: ₹1950
"""
#program 1
"""
units = int(input("Enter units: "))
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + (units - 100) * 7
else:
    bill = (100 * 5) + (100 * 7) + (units - 200) * 10
print("Total Electricity Bill=", bill)
"""

"""
2. College Result Processing System

A college wants to generate grades for students automatically based on their marks in an exam. The grading criteria are as follows:

90 and above 'n Grade A

75 to 89 'n Grade B

:

60 to 74 'n Grade C

50 to 59 'n Grade D

Below 50 'n Fail

Write a Python program to display the grade of a student.

Input:

Enter marks: 67

Output:

Grade: C
"""

# program 2
"""
marks = int(input("Enter marks: "))
if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "Fail"
print("Grade:", grade)
"""

"""
3. Income Tax Department System

The Income Tax Department needs a system to calculate tax payable by citizens based on 
their annual income:

Up to 2,50,000 'n No tax

₹2,50,001 to ₹5,00,000 'n 5% tax

₹5,00,001 to ₹10,00,000 'n 20% tax

Above ₹10,00,000 'n 30% tax

Write a Python program to calculate the tax amount.

Input:

Enter annual income: 800000

Output:

Tax Payable: ₹110000
"""


# program 3
"""
income = int(input("Enter annual income: "))
if income <= 250000:
    tax = 0
elif income <= 500000:
    tax = income * 0.05
elif income <= 1000000:
    tax = income * 0.20
else:
    tax = income * 0.30
print("Tax Payable:=", tax)
"""

"""
4. E-Commerce Discount Engine

An online shopping platform provides discounts to customers based on their total purchase 
amount:

Above ₹5000 'n 20% discount

₹2000 to ₹5000 'n 10%

discount

Below ₹2000 'n 5% discount

Write a Python program to calculate the final amount after discount.

Input:

Enter purchase amount: 4500

Output:

Final Amount: ₹4050
"""

#program 4
"""
amount = int(input("Enter purchase amount: "))
if amount > 5000:
    final = amount * 0.80
elif amount >= 2000:
    final = amount * 0.90
else:
    final = amount * 0.95
print("Final Amount: =", final)
"""

"""
5. Cinema Ticket Booking System

A cinema hall charges ticket prices based on the age of the customer:

Children (below 12 years) 'n ₹100

Adults (12 to 60 years) 'n ₹200

Senior citizens (above 60 years) 'n ₹150

Write a Python program to determine the ticket price.

Input:

Enter age: 10

Output:

Ticket Price: ₹100
"""


#program 5
"""
age = int(input("Enter age: "))
if age < 12:
    print("Ticket Price:=100")

elif age <= 60:
   print("Ticket Price:=200")
else:
    print("Ticket Price:= 150")
"""

"""
6. Company Bonus Distribution System

A company wants to calculate bonuses for employees based on their years of experience:

More than 10 years 'n 20% bonus

5 to 10 years 'n 10% bonus

2 to 5 years 'n 5% bonus

Less than 2 years 'n No bonus

Write a Python program to calculate the bonus amount.

Input:

Enter salary: 50000

Enter years of experience: 6

Output:

Bonus Amount: ₹5000
"""

# program 6
"""
salary = int(input("Enter salary: "))
years = int(input("Enter years of experience: "))
if years > 10:
    bonus = salary * 0.20
elif years >= 5:
    bonus = salary * 0.10
elif years >= 2:
    bonus = salary * 0.05
else:
    bonus = 0
print("Bonus Amount: =", bonus)
"""

"""
7. Banking Withdrawal Limit System

:

A bank wants to set withdrawal limits based on the available account balance:

Balance less than ₹1000 'n Withdrawal not allowed

₹1000 to ₹5000 'n Maximum withdrawal ₹1000

Above ₹5000 'n Maximum withdrawal ₹5000

Write a Python program to display the withdrawal limit.

Input:

Enter account balance: 3500

Output:

Maximum Withdrawal Limit: ₹1000
"""


# program 7
"""
balance = int(input("Enter account balance: "))
if balance < 1000:
    limit = 0
    print("Withdrawal not allowed")
elif balance <= 5000:
    limit = 1000
    print("Maximum Withdrawal Limit:", limit)
else:
    limit = 5000
    print("Maximum Withdrawal Limit:", limit)
    """
    
    
   
"""
8. Weather Monitoring System

A weather monitoring system classifies the weather condition based on temperature:

* Below 0°C → Freezing
* 0°C to 20°C → Cold
* 21°C to 35°C → Warm
* Above 35°C → Hot

Write a Python program to classify the weather.

Input:
Enter temperature: 38

Output:
Weather Condition: Hot

"""
# program 8
"""
t=int(input("Enter temperature: "))

if t<0:
    print("Weather Condition: Freezing")
elif t<=20:
    print("Weather Condition: Cold")
elif t<=35:
    print("Weather Condition: Warm")
else:
    print("Weather Condition: Hot")
    
"""    
    
    
    
"""
9. Student Attendance Eligibility System

A college determines whether a student is eligible to sit for exams based on attendance
 percentage:

* 75% and above → Eligible
* 60% to 74% → Eligible with warning
* Below 60% → Not eligible

Write a Python program to check eligibility.

Input:
Enter attendance percentage: 58

Output:
Status: Not Eligible

"""
# program 9
"""
att=int(input("Enter attendance percentage: "))

if att>=75:
    print("Status: Eligible")
elif att>=60:
    print("Status: Eligible with warning")
else:
    print("Status: Not Eligible")
    
"""    
    
    
    
"""
10. Mobile Data Plan Advisor

A telecom company suggests the most suitable data plan based on a user’s daily data usage:

* More than 3GB/day → Premium Plan
* 1GB to 3GB/day → Standard Plan
* Less than 1GB/day → Basic Plan

Write a Python program to recommend a plan.

Input:
Enter daily data usage: 0.8

Output:
Recommended Plan: Basic Plan


"""
# program 10
"""
d=float(input("Enter daily data usage: "))

if d>3:
    print("Recommended Plan: Premium Plan")
elif d>=1:
    print("Recommended Plan: Standard Plan")
else:
    print("Recommended Plan: Basic Plan")
"""    
    
    
"""
11. Railway Ticket Fare System

A railway system calculates ticket fare based on distance and travel class:

* Distance ≤100 km:
  Sleeper → ₹100, AC → ₹200
* Distance 101–500 km:
  Sleeper → ₹300, AC → ₹600
* Distance >500 km:
  Sleeper → ₹500, AC → ₹1000

Write a Python program to calculate ticket fare.

Input:
Enter distance: 350
Enter class: AC

Output:
Total Fare: ₹600


"""
# program 11
"""
d=int(input("Enter distance: "))
c=input("Enter class: ")

if d<=100:
    if c=="Sleeper":
        fare=100
    else:
        fare=200
elif d<=500:
    if c=="Sleeper":
        fare=300
    else:
        fare=600
else:
    if c=="Sleeper":
        fare=500
    else:
        fare=1000

print("Total Fare: =",fare)

"""


"""
12. Restaurant Bill with GST System

A restaurant applies GST based on the total bill amount:

* Up to ₹1000 → 5% GST
* ₹1001 to ₹5000 → 12% GST
* Above ₹5000 → 18% GST
Additionally, if the bill exceeds ₹3000, a service charge of ₹200 is added.

Write a Python program to calculate the final bill.

Input:
Enter bill amount: 4000

Output:
Final Bill Amount: ₹4680


"""
# program 12
"""
bill=int(input("Enter bill amount: "))

if bill<=1000:
    gst=bill*(5/100)
elif bill<=5000:
    gst=bill*(12/100)
else:
    gst=bill*(18/100)

total=bill+gst

if bill>3000:
    total=total+200

print("Final Bill Amount: ₹",total)

"""




"""
13. Employee Performance Appraisal System

A company evaluates employees based on performance rating (1–5):

* 5 → 25% salary hike
* 4 → 20% salary hike
* 3 → 10% salary hike
* 2 → 5% salary hike
* 1 → No hike
If salary is below ₹20000 and rating is 4 or above, an additional ₹2000 bonus is given.

Write a Python program to calculate revised salary.

Input:
Enter salary: 18000
Enter rating: 4

Output:
Revised Salary: ₹23600


"""
# program 13
"""
sal=int(input("Enter salary: "))
r=int(input("Enter rating: "))

if r==5:
    inc=sal*(25/100)
elif r==4:
    inc=sal*(20/100)
elif r==3:
    inc=sal*(10/100)
elif r==2:
    inc=sal*(5/100)
else:
    inc=0

total=sal+inc

if sal<20000 and r>=4:
    total=total+2000

print("Revised Salary: ₹",total)
"""



"""
14. Online Course Fee System

An online platform offers courses with fixed fees:

* Programming → ₹5000
* Design → ₹4000
* Marketing → ₹3000
Discount is applied based on user type:
* Student → 20% discount
* Working Professional → 10% discount
* Others → No discount

Write a Python program to calculate final course fee.

Input:
Enter course category: Programming
Enter user type: Student

Output:
Final Course Fee: ₹4000


"""
# program 14
"""
course=input("Enter course category: ")
user=input("Enter user type: ")

if course=="Programming":
    fee=5000
elif course=="Design":
    fee=4000
else:
    fee=3000

if user=="Student":
    fee=fee-(fee*20/100)
elif user=="Working Professional":
    fee=fee-(fee*10/100)

print("Final Course Fee: ₹",fee)
"""



"""
15. Smart Parking System

A smart parking system charges based on vehicle type and parking duration:

* Bike → ₹10/hour
* Car → ₹20/hour
* Bus → ₹50/hour
If parking duration exceeds 5 hours, an additional ₹100 penalty is applied.

Write a Python program to calculate total parking fee.

Input:
Enter vehicle type: Car
Enter hours parked: 6

Output:
Total Parking Fee: ₹220
"""
#program 15
v=input("Enter vehicle type: ")
h=int(input("Enter hours parked: "))

if v=="Bike":
    rate=10
elif v=="Car":
    rate=20
else:
    rate=50

total=rate*h

if h>5:
    total=total+100

print("Total Parking Fee: ₹",total)
