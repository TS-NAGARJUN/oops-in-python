# args allows a method to accept a variable number of positional arguments.
# kwargs allows a method to accept a variable number of keyword arguments.

def add(*args, **kwargs):
    """
    This function takes a variable number of positional and keyword arguments.
    It returns the sum of all positional arguments and prints the keyword arguments.
    """
    # Sum all positional arguments
    total = sum(args)
    
    # Print keyword arguments
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    
    return total

add(1, 2, 3, 4, 5, name="John", age=30)  # Output: name: John, age: 30
print(add(1, 2, 3, 4, 5, name="John", age=30))  # Output: 15
add(name="John", age=30 , address = "New York") # Output: name: John, age: 30, address: New York
#So args take up a tuble as input and kwargs take up a dictionary as input.