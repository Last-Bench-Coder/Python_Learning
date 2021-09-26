x = 5
y = 10

# also we can create like this
x, y = 10, 20
print(x, y)

# tuple
t = (10, 20, 30)

# Or

t = 10, 30, 40
print(t)

x, y, z = t
print(x, y, z)

# assign first value to one variable and all other for another variables
head, *tail = [1, 2, 3, 4, 5, 6]
print(head)
print(tail)

# similarly assign all values to first variable and last one for another variables
*head, tail = [1, 2, 3, 4, 5, 6]
print(head)
print(tail)

#Display as seperate values
print(*head)
