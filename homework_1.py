# 1
# Sort list
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort();
print(grades)

# Average
average = sum(grades) / len(grades)
print(average)

# Replace under 80 to failed
grades[:3] = ['Failed', 'Failed', 'Failed']
print(grades)



