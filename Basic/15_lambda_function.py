# lambda function is a different type function which does not have name
# and is only used to return values
# lambda functions are exclusively used to operate on inputs and return outputs

def add(x, y):
    return x+y


print(add(5, 7))

# OR


def add_lambda(x, y): return x+y


print(add_lambda(10, 10))

# Real Usage of Lambda function


def double(x):
    return x*2


seq = [1, 2, 3, 4, 5]
doubled = [double(x) for x in seq]
print(doubled)

# OR

doubled_lambda = list(map(lambda x: x*2, seq))
print(doubled_lambda)
