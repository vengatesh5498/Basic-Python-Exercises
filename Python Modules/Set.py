#A set is a collection which is unordered with no duplicate values.
#The syntax is {}
friend_1={"Karthi","Sujin","Parthasarathi"}
friend_2={"Suha","Navya","Pavi"}
friend_1.add("Kishore")
for x in friend_1:
    print(x)
friend_2.remove("Pavi")
for x in friend_2:
    print(x)
All=friend_2.union(friend_1)
for x in All:
    print(x)
