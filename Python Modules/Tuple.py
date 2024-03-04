#Tuple - A tuple is similar to list consisting of different inputs like float, integer and variable.
#It is used to group varialbles that are related to one another.
#Unlilke lists in '[]' it should be inside '()'
profile=("Vengatesh",27,"Male")
print(profile.count("vengatesh"))
for x in profile:
    print(x)
if "Male" in profile:
    print("He is a man")