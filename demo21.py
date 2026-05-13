#07/05/26
#assignment=21
#program 1
"""
n=int(input("Enter the limit"))

for x in range (1,n+1):
    i=1
    while i<=n:
        m=i*x
        print(x,"x" ,i ,"=", m)
        i+=1
    print()    
"""    
#program 2
"""
a=int(input("Enter the starting number:"))
b=int(input("Enter the ending number:"))
print("perfact numbers are:")

for n in range(a, b+1):
    s=0
    for i in range(1,n//2+1):
    
        if n%i==0:
            s=s+i
    if s==n:
        print(n)
     
"""
#program 3
"""
a=int(input("Enter the starting number:"))
b=int(input("Enter the ending number:")) 

print("prime numbers are:")
for n in range(a, b+1):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        #print("Prime number :", n)        
        print(n)
"""   
#program 4
"""
a=int(input("Enter the starting number:"))
b=int(input("Enter the ending number:")) 
print("Armstrong numbers are:")   
for n in range(a,b+1):
    m=n
    s=0
    l=len(str(n))
    while n>0:
        r=n%10
        s=s+r**l
        n=n//10
    if s==m:
        print(m)  
"""
#program 5
"""
a=int(input("Enter the starting number:"))
b=int(input("Enter the ending number:")) 
print("Strong numbers are:")   
for n in range(a,b+1):
    s=0
    m=n
    while n>0:
        f=1
        r=n%10
        for i in range(1, r+1):
            f=f*i
        s=s+f
        n=n//10
    if s==m:
        print(s)
 """      

#program 6
"""
a=int(input("Enter the starting number:"))
b=int(input("Enter the ending number:")) 
print("Strong numbers are:")   
for n in range(a,b+1):
    m=n
    rev=0
    while n>0:
        r=n%10
        rev=rev*10+r
        n=n//10
    if rev==m:
        print(rev)
"""

    
#program 7
"""
n1=int(input("First number"))
n2=int(input("Second number"))
for n in range(n1,n2+1):
    m=n**2
    sum=0
    while m>0:
        r=m%10
        sum=sum+r
        m=m//10
    if sum==n:
        print(n)
"""

#{Question 8}

cl=int(input("Enter number of class: "))
st=int(input("Enter number of student "))
sb=int(input("Enter number of subject "))
for a in range(1,cl+1):
    print("Class",a)
    for b in range(1,st+1): 
        print("Student",b)
        sum=0
        for c in range(1,sb+1): 
           m=int(input("Enter marks: "))
           sum=sum+m
           oprint(f"Student {b} total",sum)
