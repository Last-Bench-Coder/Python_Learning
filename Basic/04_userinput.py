#reading string value from input
name = input("Enter your name : ")
print(f"Enteren Name is {name}")

#reading numbers from input
age = input("Enter Your age : ")
#In this case we will get type error i.e. TypeError: unsupported operand type(s) for -: 'int' and 'str'
#We need to convert age to int
age_taken = int(age)
retired = (60 - age_taken)
print(f"You will get retired on {retired} age")

#reading decimal value
discount = input("Enter Hike Percentage : ")
a = float(discount)
print(f"decimal value is {a}")