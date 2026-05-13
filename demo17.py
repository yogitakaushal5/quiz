"""
#date=2/04/26
assignment=17
1. Digit Product Analyzer System

A data analytics company studies patterns in numeric transaction IDs to detect hidden behaviors.

For every entered number, the system analyzes relationships between its digits.

Write a program to:

Find the product of every pair of adjacent digits
Display all the products
Find the sum of all these products
Find the smallest product value
If the sum of products is divisible by the total number of digits, print Stable Number
Otherwise print Unstable Number

Use loops wherever required.

Input:
57294

Output:
Products: 35 14 18 36
Sum = 103
Smallest = 14
Unstable Number
"""

#program 1

"""
n=int(input("Enter number: "))

prev=n%10
n=n//10

sum_p=0
small=999

count=1

print("Products:", end=" ")

while n>0:
    curr=n%10
    p=curr*prev
    print(p, end=" ")
    
    sum_p=sum_p+p
    
    if p<small:
        small=p
    
    prev=curr
    n=n//10
    count=count+1

print()
print("Sum =", sum_p)
print("Smallest =", small)

if sum_p%count==0:
    print("Stable Number")
else:
    print("Unstable Number")
"""





"""
2. Digit Order Break Analyzer

A number validation system checks whether digits of an ID follow a strict increasing pattern. The moment the pattern breaks, the system stops further checking.

Write a program to:

Traverse the digits from left to right
Check whether each digit is greater than the previous digit
If the pattern breaks at any point, stop checking further using break
Display the position where the order breaks (1-based index)
If no break occurs, print Strictly Increasing Number

Use loops and break wherever required.

Input:
12357

Output:
Strictly Increasing Number

Input:
12342

Output:
Break at position = 4
Not Increasing Number
"""

#program 2

"""
n=int(input("Enter number: "))

rev=0
temp=n

while temp>0:
    d=temp%10
    rev=rev*10+d
    temp=temp//10

prev=-1
pos=1
flag=0

while rev>0:
    curr=rev%10
    
    if prev!=-1:
        if curr<=prev:
            print("Break at position =", pos)
            print("Not Increasing Number")
            flag=1
            break
    
    prev=curr
    rev=rev//10
    pos=pos+1

if flag==0:
    print("Strictly Increasing Number")
"""





"""
3. Zero Detection & Early Termination System

A financial system scans transaction IDs digit by digit. If a digit '0' is found, the system immediately stops processing further digits for security reasons.

Write a program to:

Traverse each digit of the number from right to left
Display each digit processed before encountering 0
Stop the loop immediately when 0 is found using break
Count how many digits were processed before termination
If no zero is found, print No Zero Found

Use loops and break wherever required.

Input:
572049

Output:
Digits Processed: 9 4
Count = 2
Zero Found - Process Stopped

Input:
56789

Output:
Digits Processed: 9 8 7 6 5
Count = 5
No Zero Found
"""

#program 3

"""
n=int(input("Enter number: "))

count=0
flag=0

print("Digits Processed:", end=" ")

while n>0:
    d=n%10
    
    if d==0:
        flag=1
        break
    
    print(d, end=" ")
    count=count+1
    
    n=n//10

print()
print("Count =", count)

if flag==1:
    print("Zero Found - Process Stopped")
else:
    print("No Zero Found")
"""





"""
4. Digit Gap Consistency Checker

A number analysis system checks whether the gap between digits follows a consistent pattern.

Write a program to:

Find the absolute difference between first two digits
Compare this difference with all next adjacent digit differences
If any difference is not equal to the first difference, stop using break
Display:
- Initial gap
- Whether all gaps are same or not

Input:
8642

Output:
Initial Gap = 2
Consistent Pattern

Input:
5321

Output:
Initial Gap = 2
Pattern Break Detected
"""

#program 4

"""
n=int(input("Enter number: "))

prev=n%10
n=n//10

curr=n%10
gap=abs(prev-curr)

print("Initial Gap =", gap)

prev=curr
n=n//10

flag=0

while n>0:
    curr=n%10
    new_gap=abs(prev-curr)
    
    if new_gap!=gap:
        print("Pattern Break Detected")
        flag=1
        break
    
    prev=curr
    n=n//10

if flag==0:
    print("Consistent Pattern")
"""





"""
5. Digit Alternating Sum System

A coding system calculates alternating sum of digits (add, subtract, add...).

Write a program to:

Traverse digits from left to right
Add first digit, subtract second, add third, and so on
Display final alternating sum
If result is positive → print Positive Pattern
Else → print Negative Pattern

Input:
1234

Output:
Result = -2
Negative Pattern

Input:
8642

Output:
Result = 8
Positive Pattern
"""

#program 5

"""
n=int(input("Enter number: "))

rev=0
temp=n

while temp>0:
    d=temp%10
    rev=rev*10+d
    temp=temp//10

pos=1
res=0

while rev>0:
    d=rev%10
    
    if pos%2!=0:
        res=res+d
    else:
        res=res-d
    
    rev=rev//10
    pos=pos+1

print("Result =", res)

if res>=0:
    print("Positive Pattern")
else:
    print("Negative Pattern")
"""