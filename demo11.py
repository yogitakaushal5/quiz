#date =23/04/26
#assignment=11

"""
1. Sum of First N Natural Numbers

A teacher wants to reward students by giving points daily. On day 1, a student gets 1 point,
 day 2 → 2 points, and so on. This follows a natural number sequence.

Write a program to calculate the total points earned after n days by summing all natural
 numbers
 up to n using loops.

Input: n = 10
Output: Total Points = 55
"""

#program 1
"""
n=int(input("Enter n: "))
s=0
for i in range(1,n+1):
    s=s+i
print("Total Points =",s)
"""




"""
2. Factorial of a Number

In project scheduling, tasks are dependent on previous tasks, and the total number of ways 
to
 arrange them is calculated using factorial.

Write a program to calculate the factorial of a given number using loops.

Input: n = 5
Output: Total Ways = 120
"""

#program 2
"""
n=int(input("Enter n: "))
f=1
for i in range(1,n+1):
    f=f*i
print("final ans =",f)
"""




"""
3. Multiplication Table

A shopkeeper wants to calculate bulk pricing for a product. If one item costs ₹n, then cost for
 multiple quantities can be calculated using multiplication.

Write a program to print the multiplication table of a given number up to 10 using loops.

Input: n = 6
"""

#program 3
"""
n=int(input("Enter number: "))
for i in range(1,11):
    print(n,"x",i,"=",n*i)
"""




"""
4. Reverse a Number

A security system stores OTP codes in reverse format for encryption.

Write a program to reverse a given integer using loops.

Input: 1234
Output: 4321
"""

#program 4
"""
n=int(input("Enter number: "))
rev=0
while n>0:
    d=n%10
    rev=rev*10+d
    n=n//10
print(rev)
"""




"""
5. Palindrome Check

A number plate is considered special if it reads the same forward and backward.

Write a program to check whether a given number is a palindrome using loops.

Input: 121
Output: Palindrome
"""

#program 5
"""
n=int(input("Enter number: "))
temp=n
rev=0
while n>0:
    d=n%10
    rev=rev*10+d
    n=n//10
if temp==rev:
    print("Palindrome")
else:
    print("Not Palindrome")
"""




"""
6. Armstrong Number (3-digit)

A 3-digit Armstrong number is one where the sum of the cubes of its digits equals the number
 itself.

Write a program to check whether a number is an Armstrong number using loops.

Input: 153
Output: Armstrong
"""

#program 6
"""
n=int(input("Enter number: "))
temp=n
s=0
while n>0:
    d=n%10
    s=s+d**3
    n=n//10
if temp==s:
    print("Armstrong")
else:
    print("Not Armstrong")
"""




"""
7. Count Even Digits

A data analyst is analyzing numeric IDs and needs to determine how many digits in the ID are 
even.

Write a program to count the number of even digits in a given number using loops.

Input: 123456
Output: Even digits count = 3
"""

#program 7
"""
n=int(input("Enter number: "))
c=0
while n>0:
    d=n%10
    if d%2==0:
        c=c+1
    n=n//10
print("Even digits count =",c)
"""




"""
8. Count Odd Digits

A banking system flags IDs with too many odd digits for further verification.

Write a program to count the number of odd digits in a given number using loops.

Input: 123456
Output: Odd digits count = 3
"""

#program 8
"""
n=int(input("Enter number: "))
c=0
while n>0:
    d=n%10
    if d%2!=0:
        c=c+1
    n=n//10
print("Odd digits count =",c)
"""




"""
9. Check All Digits Are Even

A machine only accepts numbers where every digit is even.

Write a program to check whether all digits of a number are even using loops.

Input: 2468
Output: All Even

Input: 2456
Output: Not All Even
"""

#program 9
"""
n=int(input("Enter number: "))
flag=1
while n>0:
    d=n%10
    if d%2!=0:
        flag=0
    n=n//10
if flag==1:
    print("All Even")
else:
    print("Not All Even")
"""




"""
10. Even Numbers Between Two Numbers

A teacher wants to assign only even roll numbers.

Write a program to display all even numbers between two numbers using loops.

Input: 10, 20
Output: 10 12 14 16 18 20
"""

#program 10
"""
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
for i in range(a,b+1):
    if i%2==0:
        print(i,end=" ")
"""




"""
11. Count Occurrence of a Digit

Write a program to count how many times a given digit appears in a number.

Input: Number = 122312, Digit = 2
Output: 3
"""

#program 11
"""
n=int(input("Enter number: "))
d=int(input("Enter digit: "))
c=0
while n>0:
    r=n%10
    if r==d:
        c=c+1
    n=n//10
print(c)
"""




"""
12. Multiplication of Digits

Write a program to find product of digits and check even/odd.

Input: 1234
Output: 24
Even
"""

#program 12
"""
n=int(input("Enter number: "))
p=1
while n>0:
    d=n%10
    p=p*d
    n=n//10
print(p)
if p%2==0:
    print("Even")
else:
    print("Odd")
"""




"""
13. Number Range Display System

If first number < second → ascending  
If first number > second → descending  
If equal → print message
"""

#program 13
"""
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
if a<b:
    for i in range(a,b+1):
        print(i,end=" ")
elif a>b:
    for i in range(a,b-1,-1):
        print(i,end=" ")
else:
    print("Both numbers are same")
"""




"""
14. Floor Movement System (Elevator)

Simulate elevator movement using loops.

Input: 1,5 → 1 → 2 → 3 → 4 → 5
"""

#program 14
"""
a=int(input("Enter current floor: "))
b=int(input("Enter destination: "))
if a<b:
    for i in range(a,b+1):
        print(i,end=" -> ")
elif a>b:
    for i in range(a,b-1,-1):
        print(i,end=" -> ")
else:
    print("Already on the same floor")
"""