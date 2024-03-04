#Variables and Data Types:
  variable_name = value
  integer_variable = 10
  float_variable = 3.14
  string_variable = "Hello, World!"
  boolean_variable = True

#Conditional Statements:
  if condition:
      # code block if condition is True
  else:
      # code block if condition is False
  # Example:
  if x > 0:
      print("x is positive")
  elif x == 0:
      print("x is zero")
  else:
      print("x is negative"

#Loops:
  for variable in iterable:
      # code block to be executed in each iteration
  # Example:
  for i in range(5):
      print(i)
  while condition:
      # code block to be executed while the condition is True
  # Example:
  count = 0
  while count < 5:
      print(count)
      count += 1

#Functions:
  def function_name(parameter1, parameter2):
      # code block
      return result
  # Example:
  def add_numbers(a, b):
      return a + b
  result = add_numbers(2, 3)

#Lists and Dictionaries:
  my_list = [1, 2, 3, "apple", "banana"]
  # Accessing elements
  print(my_list[0])  # prints 1
  my_dict = {"key1": "value1", "key2": 42}
  # Accessing values
  print(my_dict["key1"])  # prints "value1"

#Classes and Objects:
  class MyClass:
      def __init__(self, attribute1, attribute2):
          self.attribute1 = attribute1
          self.attribute2 = attribute2
      def my_method(self):
          # code block
  # Object instantiation
  obj = MyClass(value1, value2)
  obj.my_method()

#Exception Handling:
  try:
      # code block that might raise an exception
  except SomeException as e:
      # handle the exception
  # Example:
  try:
      result = 10 / 0
  except ZeroDivisionError as e:
      print("Error:", e)