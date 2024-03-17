#A format method is available in strings. It is optional and it gives users more conrol when displaying output.
#A classic output
Day="Tuesday"
Game="Tennis"
Pi=3.1453
Number=2000
print("I played "+Game+" on "+Day)
#Using format metod we can write the above as
print("I played {} on {}".format("Tennis","Tuesday"))
#We can also use positional arguments using index
print("I had {1} for my {0}".format("breakfast","dosa"))
#We can also write a keywork argument where we define the variable directly in the print statement
print("My name is {name} and I'm from {country}".format(country="India",name="Vengatesh"))
#Another concise way of writing this can be
Age=21
Name="Vengatesh"
text="My name is {} and I'm {} years old"
print(text.format(Name,Age))
#To add spacing within the syntax
Job="Machine Learing Engineer"
print("I'am going to be a {:>100} by the end of 2024.".format(Job))
print("I'am going to be a {:^100} by the end of 2024.".format(Job))
print("The number pi is {:.2f}".format(Pi))
print("I have {:,} rupees".format(Number))
print("I have {:b} rupees".format(Number))
print("I have {:e} rupees".format(Number))
print("I have {:E} rupees".format(Number))
print("I have {:o} rupees".format(Number))
print("I have {:X} rupees".format(Number))
print("I have {:x} rupees".format(Number))