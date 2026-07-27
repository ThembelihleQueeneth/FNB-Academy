name = input("Enter your name: ")
subject1_mark = float(input("Enter mark for subject 1: "))
subject2_mark = float(input("Enter mark for subject 2: "))
subject3_mark = float(input("Enter mark for subject 3: "))

average_mark = (subject1_mark + subject2_mark + subject3_mark) / 3

if average_mark >= 80:
    grade = "A"
elif average_mark >= 70:
    grade = "B"
elif average_mark >= 60:
    grade = "C"
elif average_mark >= 50:
    grade = "D"
else:
    grade = "E"

status = "Pass" if average_mark >= 50 else "Fail"

if subject1_mark < 40 or subject2_mark < 40 or subject3_mark < 40:
    message = "Student needs intervention"
else:
    message = "Student is doing alright"