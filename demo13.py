"""date 27/04/26
assignment=13

1. Product of Odd Numbers up to N

A puzzle game rewards players by multiplying odd numbers up to n.
Write a program using loops to find product of odd numbers.

Input:
5

Output:
15
"""

#program 1

"""
n=int(input("Enter Number: "))
product=1

for i in range(1,n+1):
    if i%2!=0:
        product=product*i

print(product)
"""




"""
2. Count Numbers Divisible by 7 Between Two Numbers

A company filters lucky coupon numbers divisible by 7.
Write a program using loops to count such numbers in range.

Input:
1 30

Output:
Count = 4
"""

#program 2

"""
a=int(input("Enter Start: "))
b=int(input("Enter End: "))
count=0

for i in range(a,b+1):
    if i%7==0:
        count=count+1

print("Count =",count)
"""




"""
3. Display Numbers Ending with 5

A supermarket tracks token numbers ending in 5.
Write a program using loops to display numbers ending with 5 between two numbers.

Input:
10 40

Output:
15 25 35
"""

#program 3

"""
a=int(input("Enter Start: "))
b=int(input("Enter End: "))

for i in range(a,b+1):
    if i%10==5:
        print(i,end=" ")
"""




"""
4. Strong Number Checker

A digital lock opens only for strong numbers.

A strong number is a number whose sum of factorial of digits equals the number.

Example:
145 = 1! + 4! + 5!

Write a program using loops to check strong number.

Input:
145

Output:
Strong Number
"""

#program 4

"""
n=int(input("Enter Number: "))
temp=n
sum=0

while n>0:
    d=n%10
    fact=1
    for i in range(1,d+1):
        fact=fact*i
    sum=sum+fact
    n=n//10

if sum==temp:
    print("Strong Number")
else:
    print("Not Strong Number")
"""




"""
5. Harshad Number Checker

A number scanner is installed in a research laboratory where thousands of numeric access codes are tested every day. To identify mathematically balanced codes, the system checks whether the entered number qualifies as a Harshad number. Numbers passing this test are considered valid for the next stage of processing.

A Harshad number is a number that is exactly divisible by the sum of its digits.

Example:
18 → 1 + 8 = 9 and 18 ÷ 9 = 2

Write a program using loops to check whether the entered number is a Harshad number.

Input:
18

Output:
Harshad Number
"""

#program 5

"""
n=int(input("Enter Number: "))
temp=n
sum=0

while n>0:
    d=n%10
    sum=sum+d
    n=n//10

if temp%sum==0:
    print("Harshad Number")
else:
    print("Not Harshad Number")
"""




"""
6. Automorphic Number Checker

A digital security company designs smart lockers that open only for special self-matching numeric codes. When a user enters a number, the system squares the number and checks whether the result ends with the same digits as the original code. If yes, the locker grants access.

An automorphic number is a number whose square ends with the same number.

Example:
25² = 625

Write a program using loops to check whether the entered number is an Automorphic number.

Input:
25

Output:
Automorphic Number
"""

#program 6
"""
num = int(input("Enter number: "))

sq = num * num
a=1
while num > 0:
    if num % 10 != sq % 10:
        a=0
    
    num = num // 10
    sq = sq // 10
if a==1:
    print("Automorphic Number")
else:
    print("Not Automorphic Number")

"""


"""
7. Duck Number Checker

A verification system is used by an e-commerce company to validate promotional coupon numbers. 
Coupon numbers containing at least one zero in between digits are considered special duck
 numbers. However, if the number starts with zero, it is rejected immediately.

A duck number is a number that contains at least one zero but does not start with zero.

Example:
1023

Write a program using loops to check whether the entered number is a Duck number.

Input:
1023

Output:
Duck Number
"""

#program 7

"""
num = int(input("Enter number: "))
zero=0 
while num>0:
    if num%10==0:
        zero=1
   num=num//10

if zero==1:
    print("Duck Number")
else:
    print("Not a Duck Number")
"""
"""
8. Mirror Difference Transaction Verification System

A multinational banking company processes thousands of daily transaction IDs. To detect 
suspicious patterns and validate system-generated IDs, the security software performs a
 Mirror 
Difference Verification Test.

For every entered transaction ID:
- Reverse the digits of the transaction ID
- Find the absolute difference between the original ID and the reversed ID
- Count the total number of digits in the difference

Apply conditions:
If difference = 0 → Perfect Match  
If divisible by 9 → Verified  
Else → Rejected

Input:
4215

Output:
Reverse = 5124
Difference = 909
Digits = 3
Verified
"""

#program 8

"""
n=int(input("Enter Number: "))
temp=n
rev=0

while n>0:
    d=n%10
    rev=rev*10+d
    n=n//10

diff=abs(temp-rev)

count=0
t=diff

if t==0:
    count=1
else:
    while t>0:
        count=count+1
        t=t//10

print("Reverse =",rev)
print("Difference =",diff)
print("Digits =",count)

if diff==0:
    print("Perfect Match")
elif diff%9==0:
    print("Verified")
else:
    print("Rejected")
"""





9. Step Difference Number Analyzer

A mathematics research center studies hidden patterns inside numbers. For every entered 
number, the system compares adjacent digits step by step.

Write a program to:
- Find absolute difference between every pair of adjacent digits
- Display all step differences
- Find sum of all differences
- Find largest difference
- Check if sum is divisible by number of digits

Input:
57294

Output:
Step Differences: 2 5 7 5
Sum = 19
Largest = 7
Unbalanced Number
"""

#program 9

"""
n=input("Enter Number: ")
sum=0
max_diff=0

print("Step Differences:",end=" ")

for i in range(len(n)-1):
    d1=int(n[i])
    d2=int(n[i+1])
    diff=abs(d1-d2)
    print(diff,end=" ")
    sum=sum+diff

    if diff>max_diff:
        max_diff=diff

print()
print("Sum =",sum)
print("Largest =",max_diff)

if sum%len(n)==0:
    print("Balanced Number")
else:
    print("Unbalanced Number")
"""