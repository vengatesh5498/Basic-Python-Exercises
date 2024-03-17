import random
x=random.randint(2,23)
y=random.random()
lists=['Rock','Paper','Scissors']
z=random.choice(lists)
cards=[1,2,3,4,5,6,7,8,9,"A","J","K","Q"]
print(x)
print(y)
random.shuffle(cards)
print(cards)
print(z)
