def greeting():
    """
    Returns a personalized greeting message with the given `name`.
    """
    name = input("What is your name? ")  # Ask for the user's name as a string

    greeting_msg = "Hello"
    return f"{greeting_msg}, {name}!"  # Include the name in the greeting

result = greeting()
print(result)  # Expected output: "Hello, [Name]"


"""
To complete this exercise:
--------------------------
Modify the 'greeting' function to return the string "hello <name>", 
where <name> is the parameter passed to the function.


Exercise Breakdown:
-------------------
Functions can receive arguments, which are variables that can be used throughout the function.
When the function is called, these arguments are assigned the values provided in the function call.

In this exercise, you will work with a function that accepts a single argument.
For instance, in the call greeting('David'), 'David' is the argument passed to the greeting function.
This argument is used within the function to generate the output.
"""
