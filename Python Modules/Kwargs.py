#KWARGS (Keyword Arguments)
#A parameter that will pack all arguments into a dictionary. It is useful so that a function can accept varying keyword arguments.

def hello(**kwargs):
    print("Hello "+ kwargs['first']+kwargs['last'])
hello(first="Vengatesh",last=" Dayalan")
