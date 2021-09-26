"""
Dictionary comprehensions is very much list comprehensions but we get a dictionary at the end of it.

Let say we have got a list of users, where each user information is stored in a tuple,
so we have a list with four user tuples inside it, they have an ID, a unique identifying number
for each user, a username and a password.

So we want to create a mapping of usernames to user information
"""

users = [
    (0, "Ramesh", "password"),
    (2, "Chakrapani", "password"),
    (3, "Upadhyaya", "password"),
    (4, "Kiran", "password")
]

username_mapping = {
    user[1]: user for user in users
}

"""
Getting the username and associating with it the entire user tuple for each of users
"""

print(username_mapping)

username_input = input("Enter username : ")
password_input = input("Enter password : ")

_,username,password = username_mapping[username_input]

if password_input == password:
    print(f"Welcome {username}")
else:
    print("Opps login failed!!!!")



