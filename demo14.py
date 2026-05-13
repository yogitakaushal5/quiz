#date=28/04/26
#assignment=14

"""
1. Prime Security Code Checker

A high-security research lab uses numeric passcodes to unlock restricted doors. Only prime
 numbers are accepted.

Write a program to check whether the entered number is Prime or Not Prime.

Input:
29

Output:
Prime Number
"""

#program 1

"""
n=int(input("Enter Number: "))
count=0

for i in range(1,n+1):
    if n%i==0:
        count=count+1

if count==2:
    print("Prime Number")
else:
    print("Not Prime Number")
"""




"""
2. Next Prime ID Generator

Find the next prime number after given number.

Input:
14

Output:
Next Prime = 17
"""

#program 2

"""
n=int(input("Enter Number: "))
num=n+1

while True:
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count=count+1

    if count==2:
        print("Next Prime =",num)
        break

    num=num+1
"""




"""
3. Composite Number Detector

Check whether number is Composite or Not.

Input:
12

Output:
Composite Number
"""

#program 3

"""
n=int(input("Enter Number: "))
count=0

for i in range(1,n+1):
    if n%i==0:
        count=count+1

if count>2:
    print("Composite Number")
else:
    print("Not Composite Number")
"""




"""
4. Prime Security Code Checker – Advanced

If prime → print next prime  
If not → print previous prime

Input:
29

Output:
Prime Number
Next Prime = 31
"""

#program 4

"""
n=int(input("Enter Number: "))
count=0

for i in range(1,n+1):
    if n%i==0:
        count=count+1

if count==2:
    print("Prime Number")
    num=n+1
    while True:
        c=0
        for i in range(1,num+1):
            if num%i==0:
                c=c+1
        if c==2:
            print("Next Prime =",num)
            break
        num=num+1
else:
    print("Not Prime Number")
    num=n-1
    while num>1:
        c=0
        for i in range(1,num+1):
            if num%i==0:
                c=c+1
        if c==2:
            print("Previous Prime =",num)
            break
        num=num-1
"""




"""
5. Next Prime ID Generator – Smart Version

Find next prime and difference.

Input:
20

Output:
Next Prime ID = 23
Gap = 3
"""

#program 5

"""
n=int(input("Enter Number: "))
num=n+1

while True:
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count=count+1

    if count==2:
        print("Next Prime ID =",num)
        print("Gap =",num-n)
        break

    num=num+1
"""




"""
6. Composite Number Detector – Risk Version

Check composite, count factors, smallest factor.

Input:
12

Output:
Composite Number
Factors Count = 6
Smallest Factor = 2
"""

#program 6

"""
n=int(input("Enter Number: "))
count=0
small=0

for i in range(1,n+1):
    if n%i==0:
        count=count+1
        if i>1 and small==0:
            small=i

if count>2:
    print("Composite Number")
else:
    print("Not Composite Number")

print("Factors Count =",count)
print("Smallest Factor =",small)
"""




"""
7. Prime Sum Lucky Number

Check sum of digits is prime or not.

Input:
4528

Output:
Sum = 19
Lucky Number
"""

#program 7

"""
n=int(input("Enter Number: "))
temp=n
sum=0

while n>0:
    d=n%10
    sum=sum+d
    n=n//10

print("Sum =",sum)

count=0
for i in range(1,sum+1):
    if sum%i==0:
        count=count+1

if count==2:
    print("Lucky Number")
else:
    print("Normal Number")
"""




"""
8. Largest Smallest Sum Prime Checker

Find largest, smallest digit and check sum prime.

Input:
57294

Output:
Largest = 9
Smallest = 2
Sum = 11
Prime
"""

#program 8

"""
n=int(input("Enter Number: "))
temp=n
maxd=0
mind=9

while n>0:
    d=n%10
    if d>maxd:
        maxd=d
    if d<mind:
        mind=d
    n=n//10

sum=maxd+mind

print("Largest =",maxd)
print("Smallest =",mind)
print("Sum =",sum)

count=0
for i in range(1,sum+1):
    if sum%i==0:
        count=count+1

if count==2:
    print("Prime")
else:
    print("Not Prime")
"""




"""
9. Even Odd Difference Prime System

Count even, odd digits and check difference prime.

Input:
123456

Output:
Even Count = 3
Odd Count = 3
Difference = 0
Not Prime
"""

#program 9

"""
n=int(input("Enter Number: "))
even=0
odd=0

while n>0:
    d=n%10
    if d%2==0:
        even=even+1
    else:
        odd=odd+1
    n=n//10

diff=abs(even-odd)

print("Even Count =",even)
print("Odd Count =",odd)
print("Difference =",diff)

count=0
for i in range(1,diff+1):
    if diff%i==0:
        count=count+1

if count==2:
    print("Prime")
else:
    print("Not Prime")
"""




"""
10. Zero Count Prime Scanner

Count zeros, sum digits, smallest digit and check final result.

Input:
908406

Output:
Zero Count = 2
Sum = 27
Smallest Digit = 0
Final Result = 0
Not Prime
"""

#program 10

"""
n=int(input("Enter Number: "))
temp=n
zero=0
sum=0
mind=9

while n>0:
    d=n%10
    sum=sum+d
    if d==0:
        zero=zero+1
    if d<mind:
        mind=d
    n=n//10

result=(zero+sum)*mind

print("Zero Count =",zero)
print("Sum =",sum)
print("Smallest Digit =",mind)
print("Final Result =",result)

count=0
if result>0:
    for i in range(1,result+1):
        if result%i==0:
            count=count+1

if count==2:
    print("Prime")
else:
    print("Not Prime")
"""