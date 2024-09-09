#Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.


def get_integer():
    user_input = input("Please enter an integer: ")
    try:
        value = int(user_input)
        return f"You entered the integer: {value}"
    except ValueError:
        raise ValueError(f"Invalid input: '{user_input}' is not a valid integer.")

# Example usage:
try:
    print(get_integer())
except ValueError as e:
    print(e)


"""Output:
          Please enter an integer: 45
          You entered the integer: 45""
