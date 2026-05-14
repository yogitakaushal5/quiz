"""
#date=05/05/26
#assignment=19
1. Smart Shopping Mall Discount System

A shopping mall offers discounts based on customer type and purchase amount.

If the customer is premium, they get 20% discount when the amount is more than 5000, otherwise 10%.
If the customer is regular, they get 10% discount when the amount is more than 3000, otherwise 5%.

Write a program to calculate the final payable amount using inline if only.
"""

#program 1

amount = float(input("Enter Amount: "))
customer = input("Enter Customer Type (premium/regular): ")

discount = amount*0.20 if customer=="premium" and amount>5000 else amount*0.10 if customer=="premium" else amount*0.10 if customer=="regular" and amount>3000 else amount*0.05

final = amount - discount

print("Final Payable Amount =", final)




"""
2. University Result Processing System

Marks ≥90 → A+
Marks ≥75 → A
Marks ≥60 → B
Marks ≥50 → C
Below 50 → Fail

Write a program using a single nested inline if expression to display the grade.
"""

#program 2

marks = int(input("Enter Marks:= "))

grade = "A+" if marks>=90 else \
        "A" if marks>=75 else \
        "B" if marks>=60 else \
        "C" if marks>=50 else "Fail"

print("Grade =", grade)




"""
3. Employee Bonus Distribution System

Experience >10 years → 30% bonus
Experience >5 years → 20% bonus
Otherwise → 10% bonus

Write a program to calculate the total salary after adding bonus using inline if.
"""

#program 3

salary = float(input("Enter Salary: "))
exp = int(input("Enter Experience: "))

bonus = salary*0.30 if exp>10 else \
        salary*0.20 if exp>5 else \
        salary*0.10

total = salary + bonus

print("Total Salary =", total)




"""
4. Electricity Billing System

Up to 100 units → ₹5 per unit
101–300 units → ₹7 per unit
Above 300 units → ₹10 per unit

Write a program to compute total bill using inline if.
"""

#program 4

units = int(input("Enter Units: "))

bill = units*5 if units<=100 else \
       units*7 if units<=300 else \
       units*10

print("Total Bill =", bill)




"""
5. Calendar System – Leap Year Checker

A year is a leap year if:
It is divisible by 400 OR
It is divisible by 4 but not by 100

Write a program using inline if to display leap year or not.
"""

#program 5

year = int(input("Enter Year: "))

result = "Leap Year" if (year%400==0 or (year%4==0 and year%100!=0)) else "Not Leap Year"

print(result)




"""
6. Data Validation System – Character Identifier

Alphabet → "Alphabet"
Digit → "Digit"
Otherwise → "Special Character"

Write a program using inline if to classify the character.
"""

#program 6

ch = input("Enter Character: ")

result = "Alphabet" if ch.isalpha() else \
         "Digit" if ch.isdigit() else \
         "Special Character"

print(result)