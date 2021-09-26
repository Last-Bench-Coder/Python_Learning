# So lets say we have got some friends Bob, Rolf and Anne and then we have two friends
# that are abroad Bob and Anne
# If only Bob and Anne are abroad. That means that Rolf must not be abroad. so the local friends are actually
# a set with a single element
friends = {"Bob", "Rolf", "Anne", "Nandu"}
abroad = {"Bob", "Anne"}

local_friends = {"Rolf"}
print(local_friends)

# instead of hard coding we are going to use thease sets to calculate who is local
# and which friends are not abroad

local_friends = friends.difference(abroad)
print(local_friends)


local_friends = abroad.difference(friends)
print(local_friends)
# if we run this we will se that we get an empty set at the bottom

# getting total friends, union - it units two sets and it gives the total of both
total_friends = friends.union(abroad)
print(total_friends)

# Scenario - Now lets say we have got a bunch of rriends some of whom study art and some of who study science
art = {"Ramesh", "Shiv", "Supriya","Bob","Dim"}
science = {"Bob", "Jim", "Kim", "Dim", "Mim"}

#Which one study both subjects, so we use intersection
both_study = art.intersection(science)
print(both_study)
