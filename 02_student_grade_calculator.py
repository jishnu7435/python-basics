marks = [float(input(f"Mark {i}: ")) for i in range(1, 6)]
total = sum(marks)
percentage = total / len(marks)
if percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "E"
print("Total:", total)
print("Percentage:", percentage)
print("Grade:", grade)
