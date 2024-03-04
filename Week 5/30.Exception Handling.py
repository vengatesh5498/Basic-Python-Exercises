try:
    numerator= int(input("Enter a number to be divided: "))
    denominator= int(input("Enter a number to be divided with: "))
    result=numerator/denominator
except ZeroDivisionError as e:
    print(e)
    print("Value of zero is not accepted")
except ValueError as e:
    print(e)
    print("Only enter numbers")
except Exception as e:
    print(e)
    print("Something went wrong")
else:
    print(result)
finally:
    print("This will always execute")
