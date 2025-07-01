def grade_checker(score):
    if score >= 90:
        return("Grade A well Done!")
    elif 75 <= score <= 89 :
        return("Grade B")
    elif 50<= score <= 74 :
         return("Grade C")
    else :
        return("Fail")
score = int(input("enter your score"))
grade_checker(score)
    
    

    
    
    
    



   


