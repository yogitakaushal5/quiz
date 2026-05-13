"""
 date=29/04/26
 assignment=15

1. Triple Operation Prime Verification System

A cybersecurity company generates a security score from entered access code.

Write a program to:

- Find sum of digits of the number
- Reverse the number
- Find absolute difference between original number and reverse
- Add digit sum and difference
- Check whether final result is Prime or Not Prime

Input:
4215

Output:
Sum of Digits = 12
Reverse = 5124
Difference = 909
Final Result = 921
Not Prime
"""

#program 1

"""
n=int(input("Enter Number: "))

# sum of digits
temp=n
sum_d=0
while temp>0:
    d=temp%10
    sum_d+=d
    temp//=10

# reverse
temp=n
rev=0
while temp>0:
    d=temp%10
    rev=rev*10+d
    temp//=10

diff=abs(n-rev)
final=sum_d+diff

# prime check
count=0
i=1
while i<=final:
    if final%i==0:
        count+=1
    i+=1

print("Sum of Digits =",sum_d)
print("Reverse =",rev)
print("Difference =",diff)
print("Final Result =",final)

if count==2:
    print("Prime")
else:
    print("Not Prime")
"""




"""
2. Multi Stage Prime Lock System

A smart locker opens only if final derived number is prime.

Write a program to:

- Find sum of digits
- Find product of digits
- Find difference between product and sum
- Count digits in difference
- Add digit count to difference
- Check whether final result is Prime or Not

Input:
234

Output:
Sum = 9
Product = 24
Difference = 15
Digits = 2
Final Result = 17
Prime
"""

#program 2

"""
n=int(input("Enter Number: "))

temp=n
sum_d=0
prod=1

while temp>0:
    d=temp%10
    sum_d+=d
    prod*=d
    temp//=10

diff=prod-sum_d

# count digits
temp=diff
count_d=0
while temp>0:
    count_d+=1
    temp//=10

final=diff+count_d

# prime
c=0
i=1
while i<=final:
    if final%i==0:
        c+=1
    i+=1

print("Sum =",sum_d)
print("Product =",prod)
print("Difference =",diff)
print("Digits =",count_d)
print("Final Result =",final)

if c==2:
    print("Prime")
else:
    print("Not Prime")
"""




"""
3. Perfect Number Reward System
"""

#program 3

"""
n=int(input("Enter Number: "))
sum_f=0

for i in range(1,n):
    if n%i==0:
        sum_f+=i
else:
    if sum_f==n:
        print("Reward Unlocked")
    else:
        print("Try Again")
"""




"""
4. Unique Digit Security Scanner
"""

#program 4

"""
n=input("Enter Number: ")
flag=1

for i in range(len(n)):
    for j in range(i+1,len(n)):
        if n[i]==n[j]:
            flag=0
            break

if flag==1:
    print("Valid Unique Code")
else:
    print("Invalid Code")
"""




"""
5. Number Stability Analyzer
"""

#program 5

"""
n=input("Enter Number: ")
flag=1

for i in range(len(n)-1):
    if int(n[i])>=int(n[i+1]):
        flag=0
        break

if flag==1:
    print("Stable Number")
else:
    print("Unstable Number")
"""




"""
6. Next Prime Cabin Number Generator
"""

#program 6

"""
n=int(input("Enter Number: "))

num=n+1
while True:
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:
        print("Next Prime Cabin =",num)
        break
    num+=1
"""




"""
7. Alternate Digit Prime Checker
"""

#program 7

"""
n=int(input("Enter Number: "))
sum_alt=0
pos=0

while n>0:
    d=n%10
    if pos%2==0:
        sum_alt+=d
    pos+=1
    n//=10

# prime check
count=0
for i in range(1,sum_alt+1):
    if sum_alt%i==0:
        count+=1

print("Alternate Sum =",sum_alt)

if count==2:
    print("Prime")
else:
    print("Not Prime")
"""




"""
8. ATM Note Counter
"""

#program 8

"""
amt=int(input("Enter Amount: "))
notes=0

while amt>=100:
    amt-=100
    notes+=1

print("Notes =",notes)
"""




"""
9. Bike Service Kilometer Checker
"""

#program 9

"""
km=int(input("Enter KM: "))
i=3000

while i<=km:
    print(i,end=" ")
    i+=3000
"""




"""
10. Lift Mode Operation – Advanced Smart Elevator System
"""

#program 10

"""
mode=int(input("Enter Mode: "))

if mode==1:
    c=int(input("Enter Current Floor: "))
    d=int(input("Enter Destination Floor: "))
    while c<=d:
        print(c,end=" ")
        c+=1

elif mode==2:
    c=int(input("Enter Current Floor: "))
    d=int(input("Enter Destination Floor: "))
    while c>=d:
        print(c,end=" ")
        c-=1

elif mode==3:
    d=int(input("Enter Destination Floor: "))
    i=0
    while i<=d:
        print(i,end=" ")
        i+=2

else:
    i=1
    while i<=4:
        print("Emergency Alarm")
        i+=1
"""