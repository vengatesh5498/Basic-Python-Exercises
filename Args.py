# *Args is a parameter that will pack all arguments int0 a tuple.
# It is useful so that a function can accept varying amount of arguments
# Should always be preceeded with *
def add(*args):
    sum=0
    args=list(args)
    args[0]=0
    for i in args:
        sum+=i
    return sum
print(add(2,5,4.45,2))