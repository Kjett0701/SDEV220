# Author: Kavon Jett 
# File name: student_gpa_checker.py 
# Description: This code is tp check a studen's GPA and see if they qualify for the Dean's list or the honor roll.  


last_name = input("What is your last name? ")  
if last_name == "ZZZ":
    print("Goodbye!")
else:
    first_name = input("What is your first name? ") 
        
        
    gpa = float(input("What is your GPA? ")) 

    if gpa >= 3.5:
        print(f"{first_name} {last_name} has made the Dean's List! ") 
    elif gpa >= 3.25: 
        print(f"{first_name} {last_name} has made the honor roll! ")  
    else:
        print(f"{first_name} {last_name} has not made the requirements of honor roll or the Dean's list. ")




