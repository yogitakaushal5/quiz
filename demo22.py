#date=08/06/26

#assignment=22
#program 1
"""
a=int(input("enter the first number"))
b=int(input("enter the second number"))
for n in range(a,b+1):
    s=0
    while n>0:
        if n%9==0:
            s=s+n
    print(s)
or
"""
#program 1
"""
i=100
s=0
while i<=200:
    
    if i%9==0:
        s=s+i
        
    i+=1
print("sum",s)       
"""
"""
#program 2
n=int(input("enter the number"))
i=1
while i<=n:
    sq=i*i
    print("sq of",i, "=",sq)
    cu=i*i*i
    print("cube of",i ,"=",cu)
    root=i**0.5
    print("sq root of",i ,"=",root)
    i+=1
"""
     
#program 3
"""
a=int(input("enter the first year."))
b=int(input("enter the second year"))
for n in range(a, b+1):
    
    if (n%4==0)and (n%100!=0)or(n%400==0):
        print("leap year=", n)
"""

#program 4
"""
n=int(input("enter the n"))
i=1
while i<=n:
    print()
    j=1
    while j<=i:
        if i%2==0:
            print("0",end=" ")
        else:
            print("1",end=" ")
        j+=1
    i+=1    
"""

"""
#progame 10

n=int(input("enter the n"))
i=0
while i<n:
    print()
    j=0
    while j<=i:
        print(j,end=" ")
        j=j+1
    i+=1        
"""
"""    
#program 5
n=int(input("enter the n"))
i=1
while i<=n:
    print()
    j=1
    ch=65
    while j<=i:
        print(chr(ch),end=" ")
        ch=ch+1
        j=j+1
    i=i+1
"""

#program 6        
"""     
n=int(input("enter the n"))
i=1
while i<=n:
    print()
    j=1
    ch=97
    while j<=i:
        print(chr(ch),end=" ")
        ch=ch+1
        j=j+1
    i=i+1
"""
#program 6

"""
    *
   **
  ***
 ****
*****
""" 
"""
n=int(input("enter the n"))
i=1
while i<=n:
    print()
    j=n-i
    while j>=1:
        print(" ",end=" ")
        j=j-1  
    j=1
    while j<=i:
        print("*",end=" ")
        j=j+1
    i=i+1
    
"""
#program 8
n=int(input("enter the n"))

i=1
while i<=n:
    print()
    j=n-i
    while j>=i:
        print("5")
        j=j-1
    i=i+1    
"""
    j=6
    while j>=i:
        print(j,end=" ")
        j=j-1
    i=i+1
         
"""
        
    
    