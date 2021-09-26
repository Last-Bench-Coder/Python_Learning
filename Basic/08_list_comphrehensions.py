# It is great feature of python and allows us to create new lists on the fly from existing lists
numbers = [1, 5, 4]

# Here we got a list of numbers and I want to end up with these numbers but multiplied by two
doubled = []

# traditional way is
for num in numbers:
    doubled.append(num * 2)

print(doubled)

# Or in another way is below
#bacause list comphrehension are usually in a single line

doubled = [num * 2 for num in numbers]
print(doubled)

#item which start with s
products = ["samsung","nokia","motorola","redmi","spice","jio","apple","lenovo"]
start_s = []

#traditional way
for x in products:
    if x.startswith("s"):
        start_s.append(x)

print(start_s)

#Or in other way
start_s=[x for x in products if x.startswith("s")]
print(start_s)