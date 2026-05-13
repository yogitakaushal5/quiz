"""
i=0
while i<=10:
    print(i)
    if i==5:
        print("find")
        break
    i+=1
"""
"""
for i in range(1,11):
    print(i)
    if i==5:
        print("use of break ")
        break
"""
"""
while true:
    password=input("enter the password")
    if password=="admin":
        """


    

#date 05/05/26
#examples    
"""    
x=30 if 101<20 else 40
print(x)
"""
"""
n=int(input("enter the number"))
if n%2==0:
    print("number is even")
else:
    print("number is odd")
   """
   
"""
n=int(input("enter the number"))
result="even" if n%2==0 else "odd"  
print(result)
"""
"""
a=int(input("enter the number "))
b=int(input("enter the number "))
max=a if a>b else b
print(max)
"""
"""
a=int(input("enter the number "))
b=int(input("enter the number "))
print("a is greter" )if a>b else print("b is greter")
"""
"""
x=10 if 20<30 else 40 if 50<60 else 70
print(x)
"""
"""
x=10 if 30>40 else 50 if 60<10 else 60
print(x)
"""
"""
a=10
b=20
c=40
max=a if a>b and a>c else b if b>c else c
print(max)
"""
"""
a=int(input("enter the number"))
b=int(input("enter the number"))
print("equal" if a==b else "a is greter" if a>b else "b is greter")
"""
"""

i=1
while i<=10:
    print(i,"is even") if i%2==0 else print(i,"is odd")
    i+=1
    
"""
"""
i=1
while i<=10:
    print(i,"even" if i%2==0 else "odd")
    i+=1
"""
"""
a=int(input("enter the number"))
match a:
    case 1:
        print("one")
    case 2:
        print("two")
    case _:
        print("wrong choice")
       
"""
"""
#program 1
amt=int(input("enter the amount :"))
cus=input("enter the customer type:")
if cus=="premium":
   print("20% discount" if amt>5000 else "10% discount")
else:
    print("10% discount" if amt>3000 else "5% discount")
    
    
"""
"""
#program 2
m=int(input("enter the marks"))
grade= "A+" if m>=90 else "A" if m>=75 else "B" if m>=60 else "C" if m>=50 else fail
print(grade)

"""
"""
#program 3
ex=int(input("enter the experience"))
sal=int(input("enter the salary"))

print("30% bonus",sal+(sal*0.3) if ex>10 else "20% bonus", sal+(sal*0.2) if ex>5 else 
"10% bonus",sal+(sal*0.1)) 
"""

#date 6/5/26
"""
a=int(input("enter the number"))
match a:
    case 3:
        print("three")
    case 1:
        print("one")
    case _:
        print("wrong")
        
print("out of match case")
"""
"""
a=int(input("enter the choice"))
match a:
    case 0:
        print("zero")
    case 1:
        print("one")
    case 2|3|4:
        print("t or f or f")
    case _:
        print("wrong")
print("out of the loop")
"""
"""
day=input("enter the number")
match day:
    case "monday":
        print("start")
    case "tuesday":
        print("stop")
    case _:
        print("wrong")
print("out of the loop")
"""
"""
a=int(input("enter the number"))
match a%2:
    case 0:
        print("even")
    case 1:
        print("odd")
   
    case _:
        print("wrong")
print("out of the loop")
"""
"""
a=int(input("enter the first no."))
b=int(input("enter the second no."))
op=input("enter the operator")
match op:
    case "+":
        print("result",(a+b))
    case "-":
        print("result",(a-b))
    case "*":
        print("result",(a*b))
    case "/":
        if b!=0:
            print("result",(a/b))
        else:
            print("avoid zero")
            
print("out of the loop")
"""
"""
ch=input("enter vowels or conso").lower()
match ch:
    case "a" |"e"|"i"|"o"|"u":
        print("vowel")
    case "#"|"%"|"$":
        print("special symbol")
    case _:
        print("coso")
print("out of the loop")
"""
"""       
age=int(input("enter the age"))
match age:
    case x if x<13:
        print("child")
    case x if x<20:
        print("teen")
    case x if x<50:
        print("adult")
print("out of the loop")
"""
"""
while True:
    print("Menu")
    print("1. ADD two numbers ")
    print("2.check even or odd")
    print("3.find square")
    print("4.exit")
    choice=int(input("enter the choice"))
    match choice:
        case 1:
            a=int(input("enter first no."))
            b=int(input("entoer second no."))
            print("sum is",(a+b))
        case 2:
            a=int(input("enter the number"))
            if a%2==0:
                print("even")
            else:
                print("odd")
        case 3:
            a=int(input("enter the number"))
            s=a*a
            print("Square is ",s)
                
                
        case 4:
            print("exiting code")
            break
"""
            
            
#date 07/06/26
"""
s=1
while s<=3:
    print("student",s)
    subject=1
    while subject<=5:
        print("subject",subject,end=" ")
        subject=subject+1
    s=s+1
    print()
"""
"""
s=1
while s<=3:
    print("student",s)
    subject=1
    while subject<=5:
        print("subject",subject,end="")
        chapter=1
        while chapter <=4:
            print("chapter",chapter,end=" ")
            chapter=chapter+1
        print()
        subject=subject+1
    s=s+1
    print()    
"""
"""
n=int(input("enter n"))
i=1
while i<=n:
    print()
    j=1
    while j<=i:
        print(j,end="")
         j=j+1
    i=i+1
"""
"""
n=int(input("enter the n"))
i=n
while i>=1:
    print()
    j=i
    while j>=1:
        print(j,end="")
        j=j-1
        
    i=i-1
"""
"""
n=int(input("enter the n"))
i=1
while i<=n:
    print()
    j=i
    while j<=n:
        print(j,end="")
        j=j+1
    i=i+1
    
    
"""
"""
n=int(input("enter the n"))
i=1
while i<=n:
    print()
    j=1
    while j<=i:
        print(i,end=" ")
        j=j+1
    i=i+1
"""
"""
n=int(input("enter the n"))
i=1
while i<=n:
    print()
    j=1
    while j<=i:
        if j%2==0:
            print("*", end=" ")
        else:
            print(j,end=" ")
            
        j=j+1
    i=i+1
        
    
"""


print("hellow",end="2n")





