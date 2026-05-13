#date=18/04/26
#assignment=7
"""
1. A bank wants to automate its loan approval process. The system should take salary, 
credit score, and number of existing loans as input. If the salary is greater than or equal to 
30000, 
then it should check the credit score. If the credit score is greater than or equal to 750,
the loan should be approved. Otherwise, it should check the number of existing loans. 
If the existing loans are less than 2, the loan should be conditionally approved; otherwise, 
it should be rejected. 
If the salary is less than 30000, the loan should be rejected. Display the final loan status.

Input:
Salary = 40000
Credit Score = 720
Existing Loans = 1

Output:
Loan Status = Conditional Approval
"""
"""
sal=int(input("enter the salary: "))
cs=int(input("enter the credit score"))
loan=int(input("enter existing loan"))
if sal>=30000:
	if sal>=750:
		print("loan approved")
	else:
		if loan<2:
			print("loan conditionally approved")
		else:
			print("loan rejected")
else:
	print("loan rejected")
"""

"""
2. An e-commerce website provides discounts based on the cart value and user type. 
The system should take cart value and user type (premium or regular) as input.
 If the cart value is greater than or equal to 5000, then check the user type. If the user is
 premium,
 apply a 20% discount; otherwise, apply a 10% discount. If the cart value is less than 5000, 
then check if it is greater than or equal to 2000. If yes, apply a 5% discount; otherwise, 
no discount is applied. Display the final payable amount.

Input:
Cart Value = 6000
User Type = Premium

Output:
Final Amount = 4800
Output:
Final Amount = 4800
"""

"""
cart=int(input("Enter Cart Value: "))
user=input("Enter User Type: ")

if cart>=5000:
    if user=="premium":
        amt=cart-(cart*20/100)
        print(" 20% discount  final amount", amt)
    else:
        amt=cart-(cart*10/100)
        print("10% discount  final amount",amt)
else:
    if cart>=2000:
        amt=cart-(cart*5/100)
        print("5% discount final amount",amt)
        
    else:
        amt=cart
        print("no discount")

"""

"""
3.A smart electricity monitoring system categorizes usage levels for better energy management.

The system should take the number of units consumed as input. If the units are greater than or 
equal to 100, then check further.
If the units are greater than or equal to 300, assign "High Usage". Otherwise, check again.
 If the units are greater than or equal to 200, assign "Moderate Usage"; otherwise, assign
"Normal Usage".
If the units are less than 100, assign "Low Usage". Display the usage category.

Input: Units = 220

Output: Usage Category = Moderate Usage
"""

"""
units=int(input("Enter Units: "))

if units>=100:
    if units>=300:
        print("Usage Category = High Usage")
    else:
        if units>=200:
            print("Usage Category = Moderate Usage")
        else:
            print("Usage Category = Normal Usage")
else:
    print("Usage Category = Low Usage")
"""

"""
4. A gym provides personalized plans based on age, weight, and fitness goal.

The system should take age, weight, and goal (weight loss or muscle gain) as input. If the age
is greater than or equal to 18, then check the weight. If the weight is greater than or equal 
to 80, then check the goal. If the goal is "weight loss", assign "Cardio Plan"; otherwise, 
assign "Strength Plan". If the weight is less than 80, assign "General Fitness Plan". If the
 age is less than 18, display "Not Allowed". Display the recommended plan.

Input:

Age = 25

Weight = 85

Goal weight loss

Output:

Plan = Cardio Plan
"""

"""
age=int(input("Enter Age: "))
wt=int(input("Enter Weight: "))
goal=input("Enter Goal(weight loss): ")

if age>=18:
    if wt>=80:
        if goal=="weight loss":
            print("Plan = Cardio Plan")
        else:
            print("Plan = Strength Plan")
    else:
        print("Plan = General Fitness Plan")
else:
    print("Not Allowed")
"""
"""
5.An ATM system processes withdrawal requests. The system should take account balance,
 withdrawal amount, and PIN status (correct or incorrect) as input. If the balance is greater 
 than or equal to the withdrawal amount, then check the withdrawal limit. If the withdrawal 
 amount is less than or equal to 10000, then check the PIN. If the PIN is correct, display 
 "Transaction Successful"; otherwise, display "Invalid PIN". If the withdrawal amount exceeds
 10000, display "Limit Exceeded". If the balance is less than the withdrawal amount, display
 "Insufficient Balance".

Input:

Balance = 20000

Withdrawal Amount = 8000

PIN = correct

Output:

Transaction Successful
"""
"""
bal=int(input("Enter Balance: "))
amt=int(input("Enter Withdrawal Amount: "))
pin=input("Enter PIN status: ")

if bal>=amt:
    if amt<=10000:
        if pin=="correct":
            print("Transaction Successful")
        else:
            print("Invalid PIN")
    else:
        print("Limit Exceeded")
else:
    print("Insufficient Balance")
"""

"""
6.A movie theatre calculates ticket prices based on age, show time, and day type. The system
 should take age, show time (morning/evening), and day type (weekday/weekend) as input.

If the age is less than 18, then check the show time. If the show time is morning, ticket 
price is 100; otherwise, ticket price is 150. If the age is 18 or above, then check the show 
time. If the show time is evening, then check the day type. If it is weekend, ticket price is 
300; otherwise, 250. If the show time is not evening,
ticket price is 200. Display the ticket price.

Input:

Age = 25

Show Time = evening

Day = weekend

Output: Ticket Price = 300
"""
"""
age=int(input("enter the age="))
show_time=input("enter the show time(morning/evening=")
day_type=input("enter the daytype weekend/weekday)=")
if age<18:
    if show_time=="morning":
        print("ticket price is 100")
    else: 
        print("ticket price is 150")
else:
    if show_time=="evening":
        if day_type=="weekend":
            print("ticket price is 300")
        else:
            print("ticket price is 250")
    else:
        print("ticket price is 200")
        
"""

"""
7. A company calculates employee bonuses based on experience, performance rating, and salary. 
The system should take experience (in years), rating, and salary as input.
If the experience is greater than or equal to 5, then check the rating. If the rating is 
greater than or equal to 4, then check the salary.
If the salary is less than 50000, assign a 20% bonus; otherwise, assign a 10% bonus. If the 
rating is less than 4, assign a 5% bonus. If the experience is less than 5, no bonus is given. 
Display the bonus amount.

Input:

Experience = 6

Rating = 4

Salary = 40000

Output:

Bonus = 8000
"""
"""
exp=int(input("Enter Experience: "))
rate=int(input("Enter Rating: "))
sal=int(input("Enter Salary: "))

if exp>=5:
    if rate>=4:
        if sal<50000:
            bonus=sal*20/100
        else:
            bonus=sal*10/100
    else:
        bonus=sal*5/100
else:
    bonus=0

print("Bonus =",bonus)

"""

"""
ex=int(input("enter the experience ="))
r=int(input("enter the rating="))
sal=int(input("enter the salary="))
if ex>=5:
    if r>=4:
        if sal<50000:
            amt=sal*20/100
            print("20% bonus",amt)
        else:
            amt=sal*10/100
            print("10% bonus",amt)
    else:
        amt=sal*5/100        
        print("5% bonus",amt)
else: 
    print("no bonus")
"""

"""
8. A warehouse management system needs to identify the highest stock level among six different
 storage units to prioritize dispatch.
The system should take the quantity of items stored in six units as input. It should compare
 all six values using nested conditions
and determine which unit has the maximum stock. Display the highest stock value among all 
six units.

Input:
Unit1 = 120
Unit2 = 450
Unit3 = 300
Unit4 = 275
Unit5 = 500
Unit6 = 390

Output:
Highest Stock = 500
"""

"""
u1=int(input("enter first unit="))
u2=int(input("enter second unit="))
u3=int(input("enter third unit="))
u4=int(input("enter fourth unit="))
u5=int(input("enter fifth unit="))
u6=int(input("enter sixth unit="))
if u1>u2:
    if u1>u3:
        if u1>u4:
            if u1>u5:
                if u1>u6:
                    print("highest stock value=",u1)
                else:
                    print("highest stock value=",u6)
            else:
                if u5>u6:
                    print("highest stock value=",u5)
                else:
                    print("highest stock value=",u6)
        else:
            if u4>u5:
                if u4>u6:
                    print("highest stock value=",u4)
                else:
                    print("highest stock value=",u6)
            else:
                print("highest stock value=",u5)
    else:
        if u3>u4:
            if u3>u5:
                if u3>u6:
                    print("highest stock value=",u3)
                else:
                    print("highest stock value=",u6)
            else:
                print("highest stock value=",u5)
                
        else:        
            print("highest stock value =",u4)
            
else:
    if u2>u3:
        if u2>u4:
            if u2>u5:
                if u2>u6:
                    print("highest stock value=",u2)
                else:
                    print("highest stock value=",u6)
            else:
                print("highest stock value=",u5)
        else:
            print("highest stock value=",u4)
    else:
        print("highest stock value =",u3)
        
"""

                
     