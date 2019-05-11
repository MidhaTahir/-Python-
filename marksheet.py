#Marksheet Program for 9th Class Student
name = input("Enter your name: ")
roll_no = int(input("Enter your roll no.:  "))
c_b = int(input("Enter your Biology marks or Computer marks: "))
chem = int(input("Enter your Chemistry marks: "))
eng = int(input("Enter your English marks: "))
sindhi = int(input("Enter your Sindhi marks :"))
pst = int(input("Enter your Pakistan Studies marks: "))
marks_obt = chem+eng+sindhi+pst+c_b
print("You have obtained " + str(marks_obt) + " marks in your exams")
percentage = float((marks_obt/500)*100)
print("Your percentage result is " + str(percentage))
if percentage>=80:
    print("Congratulations! you got A1 Grade.")
elif percentage<80 and percentage>=70:
    print("Congratulations! you got A Grade.")
elif percentage<70 and percentage>=60:
    print("You got B Grade.")
else:
    print("You are Fail")


