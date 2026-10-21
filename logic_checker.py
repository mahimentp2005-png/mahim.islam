print("Welcome to Smart Eligibility & Performance Checker\n")
name= input("Please enter your name: ") 


import sys
age= int(input("\nPlease enter your age: "))
if not age>=18:
 print("invalid age detected! Exiting the platform...")
 sys.exit()


score= float(input("\nPlease enter your score: "))
if not 0<=score<=100:
 print("invalid score detected! Exiting the platform...")
 sys.exit()

income=float(input("\nplease enter your monthly income:\n "))

if score>=90:
 print("Grade: A\n")
 grade="A"
elif score>=75:
 print("Grade: B\n")
 grade="B"
elif score>=60:
 print("Grade: C\n")
 grade="C"
else:
 print("Grade: Fail\n")
 grade="Fail"

if income<20000 and score>75:
 scholarship="eligible\n"
else: 
 scholarship="not eligible\n"

if age>=18:
 
 if score>=60:print("You passed the program.\n")
 else:print("You failed the program.\n")

else:print("Program access denied.\n")

print("Final Summary:\n\n")
print("your name: ", name)
print("your age: ", age)
print("your score: ", score)
print("your grade: ", grade)
print("scholarship: ", scholarship)