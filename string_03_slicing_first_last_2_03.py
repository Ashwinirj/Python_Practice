"""
3. Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.
Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Sample String : ' w'
Expected Result : Empty String
"""


name = "As"

# print(name[-2:])

if len(name) >2:
    # str1 = name[0:2]
    # # print(str1)
    # str2 = name[
    # # print(str2)
    final_string = name[0:2]+ name[-2:]
    print(final_string) 

else: 
    print(" ")