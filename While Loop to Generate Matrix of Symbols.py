while True:
    try:
        column_input = int(input("Please enter the number of columns"))
        break
    except ValueError:
        print("Please enter a valid integer")

while True:
    try:
        row_input = int(input("Please enter the number of rows"))
        break
    except ValueError:
        print("Please enter a valid integer")

symbol = input("Please enter a symbol")
for x in range(column_input):
    for y in range(row_input):
        print(symbol, end=" ")
    print()