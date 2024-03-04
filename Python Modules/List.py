# List is used to store multiple items in a single variable
# It should be listed within[] rather than () with each sting word in "" and numbers without double quotes.
# Some of the few operations that can be performed with list incluldes
# 1-Append
friends = ["Sujin","Karthi","Vijay_Balaji"]
friends.append("Dinesh")
for x in friends:
    print(x)
#2-Remove
ice_cream=[12,11,14,15,61]
ice_cream.remove(12)
for x in ice_cream:
    print(x)
#3-Pop
friends.pop()
for x in friends:
    print(x)#Has popped the appended value of Diniesh
#4-Sorting
friends.sort()
for x in friends:
    print(x)
