#30 april
#program 1
n = int(input())

temp = n
s = 0
rev = 0

while n > 0:
    d = n % 10
    s += d
    rev = rev * 10 + d
    n //= 10

diff = abs(temp - rev)
final = s + diff

print("Sum of Digits =", s)
print("Reverse =", rev)
print("Difference =", diff)
print("Final Result =", final)

prime = True
if final < 2:
    prime = False
else:
    for i in range(2, final):
        if final % i == 0:
            prime = False
            break

if prime:
    print("Prime")
else:
    print("Not Prime")
    
    
    
