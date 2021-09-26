friends = ["Sam","Samantha","Saurab"]
start_with_s = [x for x in friends if x.startswith("S")]

#compare list friends and start_with_s, bot are same value but result should be false. 
#Because two are different list
print(friends is start_with_s)
print("friends : ", id(friends)," start_with_s : ",id(start_with_s))

#if we compare data then output will be true
print(friends[0] is start_with_s[0])
