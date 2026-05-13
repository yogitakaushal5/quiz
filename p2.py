#project 2
store_username=""
store_password=""

while True:
    print("=======Login Signup System=======")
    print("1.Signup")
    print("2.Login")
    print("3.Forgot Password")
    print("4.Exit")
    
    choice=int(input("enter the choice")) 
    
    match choice:
        case 1:
            print("=====Signup=====")
            
            username=input("create username:  ")
            password=(input("create password:  "))
            
            if len(username)<4:
                print("username must be at least 4 character")
                continue
            
            if len(password)<6:
                print("password must be at least 6 character")
                continue
            
            store_username=username
            store_password=password
                
            print("signup successful")
                
        case 2:
            print("========Login==========")
            if store_username=="":
                print("please signup first")
                continue
            
            attempt=0
            while attempt<3:
                username=input("enter username: ")
                password=input("enter password: ")
                
                if username==store_username and password==store_password:
                    print("Login successful")
                    print("welcome",username)
                    break
                    
                else:
                    attempt+=1
                    print("Invalid username or password")
                    print("remaining attempt",3-attempt)
                    
            if attempt==3:
                print("too many attempts")
                print("account temporarily blocked")
                        
        case 3:
            print("=forgot password=")
            if store_username=="":
                print("no account found")
                continue
                
            user=input("enter username: ")
            if user==store_username:
                new_password=input("enter the new password:")
                
                if len(new_password)<6:
                    print("password too short")
                    continue
                store_password=new_password
                print("password reset successful")
                
            else:
                print("username not found")
                
        case 4:
            print("Thank you.....")
            break
        

        case _:
            print("Invalid choice")
            continue

            
    
    
    