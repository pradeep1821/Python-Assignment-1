physics = int(input("Physics: "))
chemistry = int(input("Chemistry: "))
biology = int(input("Biology: "))
math = int(input("Mathematics: "))
computer = int(input("Computer: "))

total = physics + chemistry + biology + math + computer
percentage = total / 5

if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
elif percentage >= 40:
    grade = "E"
else:
    grade = "F"

print("Percentage:", percentage, "Grade:", grade)
