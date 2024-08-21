"""
Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
If the given string already ends with 'ing', add 'ly' instead.
If the string length of the given string is less than 3, leave it unchanged.
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'
"""

def append_string_with_ing_or_ly(a):
    if len(a) >=3: 
        # print(a[-3:])
        if a[-3:] == "ing":
            a += "ly"
        else:
            a += "ing"
    # else:
    print("Please enter string of atleast length 3",a)

    return a

print(append_string_with_ing_or_ly("sejhgsdl"))


"""
# Define a function named add_string that takes one argument, 'str1'.
def add_string(str1):
    # Get the length of the input string 'str1' and store it in the variable 'length'.
    length = len(str1)

    # Check if the length of 'str1' is greater than 2 characters.
    if length > 2:
        # If the last three characters of 'str1' are 'ing', add 'ly' to the end.
        if str1[-3:] == 'ing':
            str1 += 'ly'
        else:
            # If the last three characters are not 'ing', add 'ing' to the end.
            str1 += 'ing'

    # Return the modified 'str1'.
    return str1

# Call the add_string function with different input strings and print the results.
print(add_string('ab'))      # Output: 'ab'
print(add_string('abc'))     # Output: 'abcing'
print(add_string('string'))  # Output: 'stringly'
"""