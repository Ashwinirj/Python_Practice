"""
4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'
"""

name = "good morning good"
first_char = name[0]
name = name.replace(first_char, '$')

print(first_char + name[1:])






# for i in range(1,len(name)-1):
#     if first_char in name:
#         name1[i] = '$'
#     else: 
#         name1[i] = name[i]

# print(name1)

