"""
salary=int(input("enter the salary:"))
credit_score=int(input("enter the credit core"))
loan=int(input("enter the existing loan"))
if salary>=30000:
	if credit_score>=750:
		print("loan status approved")
	else:
		if loan<2:
			print("loan conditionaly approved")
		else:
			print("loan rejected")
else:
	print("loan rejected")			
		
cart_value=int(input("enter the cart value"))
user_type=input(" enter user type premium or regular")
if cart_value>=5000:
    if user_type=="premium":
        print(f"20% discount {cart_value-(cart_value*20/100)}")
    else:
        print(f"10% discount {cart_value-(cart_value*10/100)}")
else:
    if cart_value>=2000:
        print(f"5% discount {cart_value-(cart_value*5/100)}")
    else:
        print("no discount is applied")
        

age=int(input("enter age:"))
weight=int(input("enter weight"))
goal=input("enter the goal is (weight loss)")
if age>=18:
    if weight>=80:
        if goal=="weight loss":
            print("cardio plan")a
        else:
            print("strength plan")
    else:
        print("general fitness plan")
else:
    print("not allowed")
    
    
bal=int(input("enter the balance="))
wd=int(input("enter the withdrawal Amount="))
pin=input("enter the pin=")
if bal>=wd:
    if wd<=10000:
        if pin=="correct":
            print("transaction successful")
        else:
            print("invalid pin")
    else:
         print("limited exceeded")
else:
     print("insufficient balance")
     
     
  age=int(input("enter the age="))
  show_time=input("enter the show time(morning/evening")
day_type=input("enter the daytype weekend/weekday)")
if age<18:
    if show_time=="morning":
        print("ticket price is 100")
    else: 
        print("ticket price is 150")
else:
    if show_time=="evening":
        if day_type=="weekend":
            print("ticket price is 300")
        else:
            print("ticket price is 250")
    else:
        print("ticket price is 200")
        
        
ex=int(input("enter the experience ="))
r=int(input("enter the rating="))
sal=int(input("enter the salary="))
if ex>=5:
    if r>=4:
        if sal<50000:
            amt=sal*20/100
            print("20% bonus",amt)
        else:
            amt=sal*10/100
            print("10% bonus",amt)
    else:
        amt=sal*5/100        
        print("5% bonus",amt)
else: 
    print("no bonus")
        
"""
"""
u1=int(input("enter first unit="))
u2=int(input("enter second unit="))
u3=int(input("enter third unit="))
u4=int(input("enter fourth unit="))
u5=int(input("enter fifth unit="))
u6=int(input("enter sixth unit="))
if u1>u2:
    if u1>u3:
        if u1>u4:
            if u1>u5:
                if u1>u6:
                    print("highest stock value=",u1)
                else:
                    print("highest stock value=",u6)
            else:
                if u5>u6:
                    print("highest stock value=",u5)
                else:
                    print("highest stock value=",u6)
        else:
            if u4>u5:
                if u4>u6:
                    print("highest stock value=",u4)
                else:
                    print("highest stock value=",u6)
            else:
                print("highest stock value=",u5)
    else:
        if u3>u4:
            if u3>u5:
                if u3>u6:
                    print("highest stock value=",u3)
                else:
                    print("highest stock value=",u6)
            else:
                print("highest stock value=",u5)
                
        else:        
            print("highest stock value =",u4)
            
else:
    if u2>u3:
        if u2>u4:
            if u2>u5:
                if u2>u6:
                    print("highest stock value=",u2)
                else:
                    print("highest stock value=",u6)
            else:
                print("highest stock value=",u5)
        else:
            print("highest stock value=",u4)
    else:
        print("highest stock value =",u3)
 """       
""" 
no. display program   
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
    i-=1
print("out of loop")
  """

"""
  
i=20
while i>=10:
    print(i)
    i=i-3
print("out of loop")
"""

"""
n=int(input("enter the number"))
sum=0
i=1
while i<=n:
    sum=sum+i
    i+=1
print("sum of n natural number is ",sum)
"""


"""
n=int(input("enter value of n:="))
i=2
while i<=n:
    print(i)
    i=i+2
    
print("out of loop")
"""
"""

n=int(input("enter the no."))
i=1
while i<=n:
    print(i)
    i+=2
print("out of loop")

"""
"""
n=int(input("enter the number:=")
i=1
while i<=10:
    print(n*i)
    i+=1
print("out of loop")
"""
"""
n=int(input("enter the number :="))
sum =0
while n>0:
    r=n%10
    sum=sum+r
    n=n//10
print("sum of digits is",sum)
"""

"""
n=int(input("enter the value of n"))
count=0
while n>0:
   count=count+1
   n=n//10
print("count is",count)
"""
"""
n1=int(input("enter value of n1 "))
n2=int(input("enter value of n2")) 
if n1<n2:
    while n1<=n2:
        print(n1)
        n1=n1+1
else:
    while n1>=n2:
        print(n1)
        n1=n1-1
print("out")
"""
"""
s="jayshree kaushal"
for x in s:
    print(x,end="")
print("out of loop")
       """
       
 
""" 
s=(input("enter the string"))
i=0
for x in s:
    print(i," is", x)
    i+=1
print("done")
"""
"""

n=input("enter the string")
for x in n:
    print(x)
        """
"""
for x in range(1,10):
    print(x)
"""
"""

for i in range(10,20):
    print(i)
print("program is done:")
 """
"""
for i in range(1 ,10, 2):
    print(i)
print("done")
"""
"""


for i in range(3,9,2):
    print(i)
print("done")
"""
"""

for i in range(2.5,9,2):
    print(i)
    
print("done")
"""

"""

for i in range(10,2,-3):
    print(i
    """
   
  
   
   
   
"""   
n =int(input("enter the number:="))
sum=0
for i in range(1,n+1):
    sum=sum+i
print("sum is ",sum)
"""
"""
n=int(input("enter the number:="))
for i in range(1,n+1):
    sum=0
    sum=sum+i
    print("sum is",sum)
"""
""" 
n=int(input("enter the number"))
for i in range(1,11):
    print(n*i)
print("out of loop")
"""


"""

n=int(input("enter the number:="))
f=1
for i in range(1,n+1):
    f=f*i
print("factorial is",f)
"""
"""
n=int(input("enter the number:="))
f=1
for i in range(n,0,-1):
    f=f*i
print("factorial is",f)
"""
"""
n=int(input("enter the no;"))
f=1
for i in range(1, n+1):
    f=f*i
print("factorial is",f)
"""
"""
import math
n=int(input("enter the no.:="))
print("factorial is ",math.factorial(n))
"""
"""

n=int(input("enter the number"))
sum=0
i=1

while i<n:
    if n%i==0:
        sum=sum+i
    i=i+1
if n==sum:
    print(n,"is perfact")
else:
    print(n,"is not perfact")
        
"""
"""
n=int(input("enter the no."))
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
if n==sum:
    print(n,"is perfect")
else:
    print(n,"is perfect")
"""
""" 
n=int(input("enter the number :="))
count=0
for i in str(n):
    count=count+1
print("count is",count)
"""
"""
n=int(input("enter the number:="))
rev=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
print("reverse no." ,rev)
"""

n=int(input("enter the number"))
rev=0
temp=n
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
if temp==rev:
    print("no. is palindrom")
else:
    print("no. is not palindrom")
    


     









    
    
    
    


    
    
    
    



 

    




    


    












    




    
  


  
      
        
  