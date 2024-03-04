#A dictionary is a changable, unorganised collection of unique key and values assigned in a syntax as
#Dictionary={Key:Value}
#It pairs fast because the values use the hash key
capitals={"Germany":"Berlin",
          "india":"New Delhi",
          "Russia":"Moscow",
          "China":"Beijing"}
#Updatind the assigned variables
capitals.update({"USA":"Washington D.C"})
print(capitals)
#Removing a key
capitals.pop("China")
print(capitals)
#Loops in a dictionary
for key,value in capitals.items():
    print(key,value)
