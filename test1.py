#date=27/04/26
#test=1


1. Mirror Difference Transaction Verification System

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

#program 1

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





2. Step Difference Number Analyzer

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

#program 2

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