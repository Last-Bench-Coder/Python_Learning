# Three different collections in Python, allows ua to store multiple values in single variable
# so them we can use them all at once or may be extract some of them individually
# [] = List () = tuples {} = Sets
l = ["chakrapani", "upadhyaya", "shraddha", "swapna", "shreshta"]
print(l)

# normal brackets we use for tuples, the key difference between list and tuples is that
# we cannot modify a tuple. Whereas we can add and remove elements from a list
# but we cannot add or remove elements from a tuple.
t = ("chakrapani", "upadhyaya", "shraddha", "swapna", "shreshta")
print(t)

# finally Sets, it very similar. but we use curlybraces instead of square or normal brackets
# And key difference between a set and other two
# is that while you can add and remove elements from a SET BUT WE CAN'T HAVE DUPLICATE ELEMENTS
s = {"chakrapani", "upadhyaya", "shraddha", "swapna", "shreshta"}
print(s)

#Also Lists and tuples keep the order of the elements
#So whenever we print  this list it will always have "chakrapani" then 
#"upadhyaya" then "shraddha" etc... But sets dont keep any order

#Access individual elements of a list or a tuple, by using subscript notation

print(l[0]) 
# It will give element with index zero, but sets might behave ugly here because it will not have any order

l[0] = "chakri"
print(l)
#updating the lisrt value, but cannot same with tuple

l.append("Ratnamma")
print(l)
#add new element to the list, again same we cannot do same for tuples

l.remove("chakri")
print(l)
#remove element from the list, again same we cannot do same for tuples

#Notice that its add and not append, when working with sets. Thats because append means "add
# at the ens", but sets don't have an "end" since they dont have order
s.add("chakri")
print(s)

s.remove("chakri")
print(s)



