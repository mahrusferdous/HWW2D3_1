students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]
students_approved = []

for grade in grades:
    if grade < 80:
        i = grades.index(grade)
        print(students[i])        
        print(grades[i])
        print(activities[i])
    else:
        students_approved.append(students[grades.index(grade)])
        
        
print(students_approved)