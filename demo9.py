#date 21/04/26
#assignment=9
"""
1. Insurance Claim Approval System

An insurance company processes claims based on policy age, claim amount, and accident type. 
The approval depends on multiple levels of verification to reduce fraud.

If the policy age is at least 2 years, then check the claim amount. If the claim amount is up 
to 50000, then check the accident type. If it is minor, approve the claim; otherwise, approve 
it with inspection. If the claim amount is between 50001 and 200000, then check the accident
 type. If it is major, approve with investigation; otherwise reject. If the claim amount 
 exceeds 200000, reject. If the policy age is less than 2 years, then check accident type. 
 If minor, reject; otherwise mark as pending review.

Input:
Policy Age = 3
Claim Amount = 120000
Accident Type = major

Output:
Claim Status = Approved with Investigation
"""
"""
#program 1

policy_age=int(input("enter policy age:= "))
claim_amount=int(input("Enter claim amount:= "))
accident_type=input("enter accident type:= ")

if policy_age>=2:
    if claim_amount<=50000:
        if accident_type=="minor":
            print("Claim Status Approved")
        else:
            print("Claim Status Approved with Inspection")
    else:
        if claim_amount<=200000:
            if accident_type=="major":
                print("Claim Status Approved with Investigation")
            else:
                print("Claim Status Rejected")
        else:
            print("Claim Status Rejected")
else:
    if accident_type=="minor":
        print("Claim Status Rejected")
    else:
        print("Claim Status Pending Review")
        

"""


"""
2. University Admission System

A university decides admission based on marks, entrance score, and category of the student.

If marks are 70 or above, then check entrance score. If entrance score is 80 or above, then
 check category. If general, admit; otherwise admit with scholarship. If entrance score is 
 less than 80, then check if marks are 85 or above. If yes, admit under management quota;
 otherwise reject. If marks are below 70, then check if category is not general and marks are 
 at least 60. If yes, check entrance score. If it is 70 or above, waitlist; otherwise reject.
 If none of these conditions match, reject.
"""

#program 2
"""
marks=int(input("enter marks:= "))
entrance_score=int(input("enter entrance score:= "))
category=input("enter category:= ")

if marks>=70:
    if entrance_score>=80:
        if category=="general":
            print("Admitted")
        else:
            print("Admitted with Scholarship")
    else:
        if marks>=85:
            print("Management quota")
        else:
            print("Rejected")
else:
    if category!="general":
        if marks>=60:
            if entrance_score>=70:
                print("Waitlisted")
            else:
                print("Rejected")
        else:
            print("Rejected")
    else:
        print("Rejected")
"""




"""
3. Smart Loan Risk Categorization

A bank categorizes loan applicants into risk levels based on salary, credit score, and number
 of existing loans.
"""

#program 3
"""
salary=int(input("enter salary:= "))
credit_score=int(input("enter credit score:= "))
existing_loans=int(input("enter existing loans:= "))

if salary>=30000:
    if credit_score>=750:
        if existing_loans==0:
            print("Low Risk")
        else:
            if existing_loans<=2:
                print("Medium Risk")
            else:
                print("High Risk")
    else:
        if salary>=50000:
            if credit_score>=650:
                print("Medium Risk")
            else:
                print("High Risk")
        else:
            print("Not Eligible")
else:
    print("Not Eligible")
"""




"""
4. E-Learning Course Access System
"""

#program 4
"""
subscription=input("enter subscription:= ")
progress=int(input("enter progress:= "))
test_score=int(input("enter test score:= "))

if subscription=="premium":
    if progress>=80:
        if test_score>=70:
            print("Certificate Unlocked")
        else:
            print("Retry Test")
    else:
        print("Complete Course")
else:
    if subscription=="basic":
        if progress>=50:
            print("Limited Access")
        else:
            print("Locked")
    else:
        print("Denied")
"""




"""
5. Smart Warehouse Dispatch System
"""

#program 5
"""
stock=int(input("enter stock:= "))
priority=input("enter priority:= ")
distance=int(input("enter distance:= "))

if stock>=100:
    if priority=="high":
        if distance<=200:
            print("Immediate Dispatch")
        else:
            print("Dispatch via Fast Courier")
    else:
        if stock>=300:
            print("Bulk Dispatch")
        else:
            print("Normal Dispatch")
else:
    if stock>=50:
        if priority=="high":
            print("Partial Dispatch")
        else:
            print("Hold")
    else:
        print("Out of Stock")
"""




"""
6. Banking Fraud Detection System
"""

#program 6
"""
transaction_amount=int(input("enter transaction amount:= "))
location=input("enter location:= ")
account_age=int(input("enter account age:= "))

if transaction_amount>=10000:
    if location=="international":
        otp=input("OTP Verified (yes/no):= ")
        if otp=="yes":
            print("Transaction Status = Allowed")
        else:
            print("Blocked")
    else:
        if transaction_amount>=50000:
            if account_age>=2:
                print("Allowed")
            else:
                print("Flagged")
        else:
            print("Allowed")
else:
    unusual=input("Unusual Activity (yes/no):= ")
    if unusual=="yes":
        print("Flagged")
    else:
        print("Allowed")
"""




"""
7. Ride Booking Surge Pricing System
"""

#program 7
"""
demand=int(input("enter demand:= "))
time=input("enter time:= ")
distance=int(input("enter distance:= "))

if demand>=80:
    if time=="peak":
        if distance>=10:
            print("Fare Multiplier = 2x Fare")
        else:
            print("Fare Multiplier = 1.5x Fare")
    else:
        if demand>=90:
            print("Fare Multiplier = 1.8x Fare")
        else:
            print("Fare Multiplier = 1.3x Fare")
else:
    if demand>=50:
        if time=="peak":
            print("Fare Multiplier = 1.2x Fare")
        else:
            print("Fare Multiplier = Normal Fare")
    else:
        print("Fare Multiplier = Normal Fare")
"""




"""
8. Smart Farming Irrigation System
"""

#program 8
"""
soil=int(input("enter soil moisture:= "))
temp=int(input("enter temperature:= "))
crop=input("enter crop type:= ")

if soil<=30:
    if temp>=35:
        if crop=="wheat":
            print("High Water Supply")
        else:
            print("Moderate Supply")
    else:
        print("Moderate Supply")
else:
    if soil<=60:
        rain=input("Rain Expected (yes/no): ")
        if rain=="yes":
            print("Delay Irrigation")
        else:
            print("Irrigation=Light Irrigation")
    else:
        print("No Irrigation")
"""




"""
9. Multi-Level Employee Promotion System
"""

#program 9
"""
exp=int(input("enter experience:= "))
rating=int(input("enter rating:= "))
projects=int(input("enter projects:= "))
salary=int(input("enter salary:= "))

if exp>=5:
    if rating>=4:
        if projects>=3:
            if salary<=50000:
                print("Promotion Status = 30% hike")
            else:
                print("Promotion Status = 20% hike")
        else:
            print("Promotion Status = Promoted with 10% hike")
    else:
        print("Promotion Status = No Promotion")
else:
    if rating==5:
        print("Promotion Status = Fast Track Promotion")
    else:
        print("Promotion Status = No Promotion")
"""




"""
10. Smart Restaurant Order Processing System
"""

#program 10
"""
amt=int(input("Enter Order Amount:= "))
cust=input("Enter Customer Type:= ")
pay=input("Enter Payment Method:= ")

if amt>=2000:
    if cust=="VIP":
        if pay=="online":
            print("Free Dessert and 20% Discount")
        else:
            print("Free Dessert")
    else:
        if amt>=5000:
            print("15%Discount")
        else:
            print("10%Discount")
else:
    if amt>=1000:
        if cust=="VIP":
            print("10% Discount")
        else:
            print("5% Discount")
    else:
        print("No Offer")
"""