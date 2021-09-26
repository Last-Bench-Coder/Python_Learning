# IT IS KEY VALUE PAIR
friends = [
    {"name": "Chakrapani U", "age": 30},
    {"name": "Shraddha U", "age": 6},
    {"name": "Shreshta U", "age": 2},
    {"name": "Swapna Y V", "age": 29}
]

print(friends)

# To display the perticula friend, we need to use the index
print(friends[1])
print(friends[1]["name"])

student_attendance = {"Chakrapani": 37, "Swapna": 30, "Shraddha": 6}

for x in student_attendance:
    print(f"{x} - {student_attendance[x]}")

# OR We can write in another way

for x, y in student_attendance.items():
    print(f"{x} - {y}")

#Check if student exists or not

student = input("Enter Student Name : ")

if student in student_attendance:
    print(f"Shraddhs Attendance is : {student_attendance[student]}")
else:
    print("Student not exists")
