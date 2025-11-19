travel_bag = ("shirt", "pants", "shoes", "underwear", "socks")

print(travel_bag[1])
print(travel_bag[3])

if "shoes" in travel_bag:
    print("You are ready to walk!")
else:
    print("you forgot your shoes!")

essentials = ("deoderant", "toothbrush", "shampoo")

final_bag = travel_bag + essentials

print(len(final_bag))

print(final_bag[-1])