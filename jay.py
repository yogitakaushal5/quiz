


#27/04/2026
#assignment=13



#program 1
n=int(input("enter the number"))
mul=1
for i in range(1,n+1):
    if i%2!=0:
	    mul=mul*i
print("multiplication",mul)
"""
"""
#program 2
n1=int(input("enter the first number:="))
n2=int(input("enter the second number:="))
count=0
for i in range(n1,n2+1):
    if i%7==0:
        count=count+1
print(count)
"""
"""

#program 3
n1=int(input("enter the first number:="))
n2=int(input("enter the second number:="))
for i in range(n1,n2+1):
    if i%5==0 and i%10!=0:
        print(i)
    
"""
#program 4
"""
n=int(input("enter the number"))
temp=n
s=0

while n>0:
    r=n%10
    f=1
    for i in range(1,r+1):
        f=f*i
    s=s+f
    n=n//10
if s==temp:
    print("strong number:")
else:
    print("not a strong number")
    """


#program 5
"""
n=int(input("Enter a number:"))
temp=n
s=0
while n>0:
    r=n%10
    s=s+r
    n=n//10
if temp%s==0:
    print("Harshad Number")
else:
    print("Not a Harshad Number")
    """
    
#program 6
"""
n=int(input("Enter a number:"))
sq=n*n
ns=str(n)
sqs=str(sq)
if sqs.endswith(ns):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
"""
#program 7
"""
n=int(input("Enter a number: "))
temp=n
z=False

while n>0:
    r=n%10
    if r==0:
        z= True
    n=n//10
if z:
    print("Duck Number")
else:
    print("Not a Duck Number")
   """
    
#program 8
"""
num=int(input("Enter transaction ID: "))
rev=0
temp=num

while temp > 0:
    digit=temp%10
    rev=rev* 10+digit
    temp=temp//10


diff=abs(num-rev)
count=0
temp=diff
if diff==0:
    count=1
else:
    while temp>0:
        temp=temp//10
        count+=1
print("Reverse =", rev)
print("Difference =", diff)
print("Digits =", count)

if diff==0:
    print("Perfect Match")
elif diff%9==0:
    print("Verified")
else:
    print("Rejected")
    """

#program 9

num = input("Enter number: ")

diffs = []  
sum_diff = 0
largest = 0
for i in range(len(num) - 1):
    d1 = int(num[i])
    d2 = int(num[i + 1])
    
    diff = abs(d1 - d2)
    
    diffs.append(diff)
    sum_diff += diff
    
    if diff > largest:
        largest = diff

print("Step Differences:", *diffs)
print("Sum =", sum_diff)
print("Largest =", largest)
digits = len(num)

if sum_diff % digits == 0:
    print("Balanced Number")
else:
    print("Unbalanced Number")















        
    
    
    
 


