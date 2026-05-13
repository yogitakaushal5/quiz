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