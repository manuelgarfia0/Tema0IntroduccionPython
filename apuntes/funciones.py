# Declaring a function with two parameters
def function(param1, param2):
    """This function takes two parameters
    and returns their sum."""
    res = param1 + param2
    return res
# Calling the function and printing the result
addition = function(2, 3)
print(addition)
# Function with a default parameter
def greet(name = "Manuel"):
    print("Hello", name)

greet("Alvaro")
greet()