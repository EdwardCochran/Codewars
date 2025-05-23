#Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.


def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    # This function checks if a number is even or odd.
    # If the number is even, it returns "Even".
    # If the number is odd, it returns "Odd".
    
    


#We need a function that can transform a number (integer) into a string.

    def number_to_string(num):
    return str(num)

# This function takes an integer as input and converts it to a string.
# It uses the str() function to perform the conversion.
# The function returns the string representation of the number.




#Write a function that removes the spaces from the string, then return the resultant string.
def no_space(input_string):
    return input_string.replace(" ", "")

# This function takes a string as input and removes all spaces from it.
# It uses the replace() method to replace spaces with an empty string.
# The function returns the modified string without spaces.