# 2
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

if attended[0] in submitted:
    print("Charlie is in the list")
else:
    print("Charlie is not in the list")
    
if attended[1] in submitted:
    print("Eve is in the list")
else:
    print("Eve is not in the list")
    
if attended[2] in submitted:
    print("Alice is in the list")
else:
    print("Alice is not in the list")
    
if attended[3] in submitted:
    print("Frank is in the list")
else:
    print("Frank is not in the list")
    
    
same_string = "All students attended" if attended == submitted else "Not all students attended"
print(same_string)


for student in attended:
    if student not in submitted:
        print(student + " did not submit the homework.")
        attended.remove(student)
        
print("Final attendance", attended)

