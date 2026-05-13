"""
30/04/26
assignment=16
1. Leap Year Event Scheduler – Multi-Year Analysis System

A city event management system schedules special festivals only in leap years.

Write a program to:
- Read start year and end year
- Check leap year using rules
- Print event status
- Count total leap years

Input:
2000
2005

Output:
2000 → Event Scheduled
...
Total Leap Years = 2
"""

#program 1

"""
start=int(input("Enter Start Year: "))
end=int(input("Enter End Year: "))

count=0

for y in range(start,end+1):
    if y%4==0:
        if y%100==0:
            if y%400==0:
                print(y,"→ Event Scheduled")
                count+=1
            else:
                print(y,"→ No Event")
        else:
            print(y,"→ Event Scheduled")
            count+=1
    else:
        print(y,"→ No Event")

print("Total Leap Years =",count)
print("Total Events Scheduled =",count)
"""





"""
2. Fibonacci Series Generator
"""

#program 2

"""
n=int(input("Enter Terms: "))

a=0
b=1

print(a,b,end=" ")

i=3
while i<=n:
    c=a+b
    print(c,end=" ")
    a=b
    b=c
    i+=1
"""





"""
3. Fibonacci Population Growth Tracker
"""

#program 3

"""
n=int(input("Enter Months: "))

a=0
b=1
total= a+b
count=0

print("Population Growth:")
print(a,b,end=" ")

i=3
while i<=n:
    c=a+b
    print(c,end=" ")
    total+=c
    if c>5:
        count+=1
    a=b
    b=c
    i+=1

print()
print("Total Population =",total)
print("Months with Population > 5 =",count)
"""





"""
4. Spy Number Detector
"""

#program 4

"""
n=int(input("Enter Number: "))
sum_d=0
prod=1

while n>0:
    d=n%10
    sum_d+=d
    prod*=d
    n//=10

if sum_d==prod:
    print("Spy Number")
else:
    print("Not Spy Number")
"""





"""
5. Automorphic Number Lock
"""

#program 5

"""
n=int(input("Enter Number: "))
sq=n*n

temp=n
flag=1

while temp>0:
    if temp%10 != sq%10:
        flag=0
        break
    temp//=10
    sq//=10

if flag==1:
    print("Automorphic Number")
else:
    print("Not Automorphic Number")
"""





"""
6. Buzz Number Detector
"""

#program 6

"""
n=int(input("Enter Number: "))

if n%7==0 or n%10==7:
    print("Buzz Number")
else:
    print("Not Buzz Number")
"""





"""
7. Adam Number Verification System
"""

#program 7

"""
n=int(input("Enter Number: "))

# reverse
temp=n
rev=0
while temp>0:
    rev=rev*10+(temp%10)
    temp//=10

sq1=n*n
sq2=rev*rev

# reverse sq1
temp=sq1
rev_sq=0
while temp>0:
    rev_sq=rev_sq*10+(temp%10)
    temp//=10

if rev_sq==sq2:
    print("Adam Number")
else:
    print("Not an Adam Number")
"""





"""
8. Trimorphic Number Analyzer
"""

#program 8

"""
n=int(input("Enter Number: "))
cube=n*n*n

temp=n
flag=1

while temp>0:
    if temp%10 != cube%10:
        flag=0
        break
    temp//=10
    cube//=10

if flag==1:
    print("Trimorphic Number")
else:
    print("Not Trimorphic Number")
"""





"""
9. Abundant Number Detector
"""

#program 9

"""
n=int(input("Enter Number: "))
sum_f=0

for i in range(1,n):
    if n%i==0:
        sum_f+=i

if sum_f>n:
    print("Abundant Number")
else:
    print("Not Abundant Number")
"""





"""
10. Electricity Bill Processing System (Multi-House)
"""

#program 10

"""
n=int(input("Enter Number of Houses: "))

total=0
highest=0

for i in range(1,n+1):
    units=int(input("Enter Units: "))
    
    bill=0
    
    if units<=100:
        bill=units*5
    else:
        if units<=200:
            bill=100*5 + (units-100)*7
        else:
            bill=100*5 + 100*7 + (units-200)*10

    if bill>2000:
        bill= bill + (bill*10/100)

    if units<50:
        bill= bill - 100

    print("House",i,"Bill =",int(bill))

    total+=bill

    if bill>highest:
        highest=bill

print("Total Collection =",int(total))
print("Highest Bill =",int(highest))
"""