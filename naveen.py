"""print("welcome")
name=input("enter name")
if name:
    print("name is :", name)
print("done")
"""
"""
#if....else
print("welcome")
name=input("enter the name")
if name:
    print("name entered is :",name)
else:
    print("name not entered")
    print("please enter")
print("done")
"""
"""
print("welcome")
a=int(input("enter the no. 1"))
b=int(input("enter second no. 2"))
if a>b:
    print("a is greater ")
else:
    print("b is greater")
print("done")
"""
"""
a=int(input("enter the first no."))
b=int(input("enter the second number"))
if a>b:
    pass
else:
    print("b is greater")
print("done")
"""
"""
print("welcome")
ch=input("enter character").lower()
if ch=="a" or ch=='e' or ch=='i' or ch=='o' or ch=='u':
    print("vowel")
else:
    print("consonent")
    
print("done")
"""
"""
#nested if else
a=int(input("enter the first number= "))
b=int(input("enter the second number="))
c=int(input("enter the third number="))
d=int(input("enter the fourth number="))
if a>b:
    if a>c:
        if a>d:
            print("a is greater")
        else:
            print("d is greater")
    else:
        if c>d:
            print("c is greater")
            
        else:
            print("d is larger")
            
else:
    if b>c:
        if b>d:
            pirnt("b is largeer")
        else:
            print("d is larger")
            
    else:
        if c>d:
            print("c is largest")
        else:
            print("d is largest")
 """
""" 
i=1
while i<=5:
     print(i)
     i+=1
print("out of loop")
"""

"""
i=10
while i>=1:
    print(i)
    i=i-1
print("out of loop")
"""

"""
n=int(input("enter the number "))
sum=0
i=1
while i<=n:
    sum=sum+i
    i+=1
print(sum)#6266872992

n=int(input("enter the one item cost"))
i=1
while i<=10:
    print(n*i)
    i+=1
 
  
  
  """
n=int(input("enter the digits:="))
sum=1
while n>0:
    rem=n%10
    sum=sum*rem
    n=n//10
print(sum)
if sum//2:
    print("even")
else:
    print("odd")
 """  
   
   
   
i=1
while i<=0:
    print(i)
    if i==5:
        print("find")
        break
    i+=1
    





