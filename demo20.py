#Program 1
#date = 06/05/26
#assignment=20
"""

while True:
    print("Menu")
    print("1.Check Prime Number")
    print("2.Check Palindrome Number")
    print("3.Check Reverse Number")
    print("4.Check Count a digit of a Number")
    print("5.Exit")
    choice=int(input("enter the choice"))
    match choice:
        case 1:
            num=int(input("enter the number"))
            c=0
            for i in range(1,num+1):
                if num%i==0:
                    c=c+1
            if c==2:
                print("Prime number")
            else:
                print(" Not a Prime number")

        case 2:
            num=int(input("enter the number"))
            temp=num
            rev=0
            while num>0:
                r=num%10
                rev=rev*10+r
                num=num//10
            if temp==rev:
                print("Palindrome Number")
            else:
                print(" Not Palindrome Number")
        case 3:
            num=int(input("enter the number"))
            temp=num
            rev=0
            while num>0:
                r=num%10
                rev=rev*10+r
                num=num//10
            print("reverse number is",rev)
        
        case 4:
            num=int(input("enter the number"))
            c=0
            while num>0:
                num=num//10
                c=c+1
            print("Total digit=", c)    
        
        case 5:
            print("Exiting program... Thank you!")
            break
"""
#program 2

"""
basic =0

while True:

    print("\n1. Enter Basic Salary")
    print("2. Calculate HRA and DA")
    print("3. Calculate Net Salary")
    print("4. Tax Deduction")
    print("5. Display Salary Slip")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            basic = int(input("Enter Basic Salary: "))
            print("Basic Salary recorded successfully")

        case 2:
            if basic==0:
                print("Please enter basic salary first")

            else:
                hra = basic * 20 / 100
                da = basic * 10 / 100

                print("HRA:", hra)
                print("DA:", da)

        case 3:
            if basic==0:
                print("Please enter basic salary first")

            else:
                net = basic + hra + da

                print("Net Salary (before tax):", net)

        case 4:
            if basic==0:
                print("Please enter basic salary first")

            else:
                if net > 50000:
                    tax = net * 10 / 100

                else:
                    tax = net * 5 / 100

                final = net - tax

                print("Tax Deduction:", tax)

        case 5:
            if basic==0:
                print("Please enter basic salary first")

            else:
                print("\n----- Salary Slip -----")
                print("Basic Salary:", basic)
                print("HRA:", hra)
                print("DA:", da)
                print("Net Salary:", net)
                print("Tax:", tax)
                print("Final Salary:", final)

        case 6:
            print("Exiting program... Thank you!")
            break

        case _:
            print("Invalid choice. Please try again.")
            
            
 """
 
 #program 3

"""
balance = 0

while True:

    print("\n1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Apply Interest")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:

            amount = int(input("Enter amount to deposit: "))
            balance = balance + amount

            print("Amount deposited successfully")

        case 2:

            if balance == 0:
                print("No balance available. Please deposit first")

            else:

                amount = int(input("Enter amount to withdraw: "))

                if amount > balance:
                    print("Insufficient balance")

                else:
                    balance = balance - amount
                    print("Withdrawal successful")

        case 3:

            if balance == 0:
                print("No balance available. Please deposit first")

            else:
                print("Current Balance:", balance)

        case 4:

            if balance == 0:
                print("No balance available. Please deposit first")

            else:

                if balance > 50000:
                    interest = balance * 5 / 100

                else:
                    interest = balance * 3 / 100

                balance = balance + interest

                print("Interest added:", interest)
                print("Updated Balance:", balance)

        case 5:
            print("Exiting system... Thank you!")
            break

        case _:
            print("Invalid choice. Please try again.")
            
            
            
 """
 
 #program 4
 
 """
units = 0

while True:

    print("\n1. Enter Units Consumed")
    print("2. Calculate Bill Amount")
    print("3. Apply Surcharge")
    print("4. Display Final Bill")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:

            units = int(input("Enter units consumed: "))

            print("Units recorded successfully")

        case 2:

            if units == 0:
                print("Please enter units consumed first")

            else:

                if units <= 100:

                    bill = units * 5

                elif units <= 200:

                    bill = (100 * 5) + ((units - 100) * 7)

                else:

                    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

                print("Bill Amount:", bill)

        case 3:

            if units == 0:
                print("Please enter units consumed first")

            else:

                if bill > 2000:

                    surcharge = bill * 10 / 100

                else:

                    surcharge = bill * 5 / 100

                total = bill + surcharge

                print("Surcharge:", surcharge)

        case 4:

            if units == 0:
                print("Please enter units consumed first")

            else:

                print("\n----- Final Bill -----")
                print("Units:", units)
                print("Bill Amount:", bill)
                print("Surcharge:", surcharge)
                print("Total Payable:", total)

        case 5:
            print("Exiting system... Thank you!")
            break

        case _:
            print("Invalid choice. Please try again.")
            
"""