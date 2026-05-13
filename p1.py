# Quiz Game

total_questions=10
while True:
    print("==========Quiz Game==========")
    print("1.Start Quiz")
    print("2.Rules")
    print("3.Exit")
    choice =int(input("enter your choice"))
    
    match choice:
        case 1:
            score=0
            print("Quiz Started")
            print("Each correct answer=1 mark")
            
            #Q.1
            print("Q.1=What is the capital of India?")
            print("1.Chennai")
            print("2.Delhi")
            print("3.Kolkata")
            print("4.Mumbai")
            ans=int(input("enter answer: "))
            
            if ans==2:
                print("correct answer")
                score+=1
            else:
                print("wrong answer")
        #Q.2:
            print("Q.2= Which keyword is used for loop in python?")
            print("1.loop")
            print("2.for")
            print("3.repeat")
            print("4.iterate")
            ans=int(input("enter answer: "))
            
            if ans==2:
                print("correct answer")
                score+=1
            else:
                print("wrong answer")
        #Q.3:
            print("Q.3= How many days are there in a week?")
            print("1. 5")
            print("2. 6")
            print("3. 7")
            print("4. 8")
            ans=int(input("enter answer: "))
            
            if ans==3:
                print("correct answer")
                score+=1
            else:
                print("wrong answer")
        #Q.4:
            print("Q.4= Which symbol is used for comments in python?")
            print("1. // ")
            print("2. # ")
            print("3. /* ")
            print("4. -- ")
            ans=int(input("enter answer: "))
            
            if ans==2:
                print("correct answer")
                score+=1
            else:
                print("wrong answer")

        #Q.5:
            print("Q.5= Which function is used for input?")
            print("1. print()")
            print("2. scan()")
            print("3. input()")
            print("4. read()")
            ans=int(input("enter answer: "))
            
            if ans==3:
                print("correct answer")
                score+=1
            else:
                print("wrong answer")
       
        # Q.6:
            print("Q.6= What is 10+20 ?")
            print("1. 10 ")
            print("2. 20")
            print("3. 30")
            print("4. 40")
            ans=int(input("enter answer: "))
            
            if ans==3:
                print("correct answer")
                score+=1
            else:
                print("wrong answer")
     
        #Q.7:
            print("Q.7= Which data type store text?")
            print("1. int ")
            print("2. float ")
            print("3. string ")
            print("4. bool")
            ans=int(input("enter answer: "))
            
            if ans==3:
                print("correct answer")
                score+=1
            else:
                print("wrong answer")
   
        #Q.8:
    
            print("Q.8= Which operator is used for multiplication?")
            print("1. + ")
            print("2. - ")
            print("3. * ")
            print("4. / ")
            ans=int(input("enter answer: "))
            
            if ans==3:
                print("correct answer")
                score+=1
            else:
                print("wrong answer")
    
    
        #Q.9:
            print("Q.9= Which company developed python?")
            print("1. Microsoft")
            print("2. Apple")
            print("3. Google")
            print("4. None")
            ans=int(input("enter answer: "))
            
            if ans==4:
                print("correct answer")
                score+=1
            else:
                print("wrong answer")
        #Q.10:
            print("Q.10= Which loop runs until condition is true?")
            print("1. for  ")
            print("2. while")
            print("3. do while ")
            print("4. nested")
            ans=int(input("enter answer: "))
            
            if ans==2:
                print("correct answer")
                score+=1
            else:
                print("wrong answer")
            
            print("=========QUIZ RESULT============")
            print("total question:" , total_questions)
            print("correct answers:",score)
            print("worong answers:",total_questions-score)
            percentage=(score/total_questions)*100
            print("percentage=",percentage)
             
            if percentage>=90:
                print("Grade : A+")
                print("Excellent")
            elif percentage>=75:
                print("Grade : A")
                print("very good")
            elif percentage>=60:
                print("Grade : B")
                print("good job")
            elif percentage>=40:
                print("Grade : C")
                print("need Improvement")
            else:
                print("Grade :fail")
                print("try next time")
                
            print("Do you want to play again?")
            print("1. yes")
            print("2. no")
            play=int(input("enter choice: "))
            if play==1:
                continue
            else:
                print("return to main menu")
        
        case 2:
            print("======Rules=======")
            print("1. Total 10 questions")
            print("2. Each question carries 1 marks")
            print("3. No negative marking")
            print("4. Enter correct option number")
            print("5. Final grade will be displayed")
            
        case 3:
            print("Thank you for playing quiz game")
          
            break
        case _:
            print("Invalid choice")
            print("Please enter the option ")
            continue
         
        
                
 