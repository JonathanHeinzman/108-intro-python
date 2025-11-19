invited_friends = {"Alex", "Sam","Leo", "Mina"}
rsvped = {"Mina", "Sam", "Jordan"}

print(invited_friends.union(rsvped))
print(rsvped)
print(invited_friends.difference(rsvped))

invited_friends.update("Jon", "Mike")

rsvped.remove("Jordan")

print(len(rsvped))

print("Leo" in rsvped)