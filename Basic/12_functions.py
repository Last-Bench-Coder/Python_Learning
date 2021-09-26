#friends = ["sam", "dam"]


#def add_friend():
#    friend_name = input("Enter your friend name : ")
#    friends = friends + [friend_name]

#add_friend()

#above code will throw the error, because friends declared already, 
#declare the variable after function creation

def add_friend():
    friend_name = input("Enter your friend name : ")
    friends.append(friend_name)
    print("Friend Added Successfully")
    print(friends)

friends = []

add_friend()