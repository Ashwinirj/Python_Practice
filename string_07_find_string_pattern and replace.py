"""   https://www.w3resource.com/python-exercises/string/

Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string.
If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
Sample String : 'The lyrics is not that poor!'
'The lyrics is poor!'
Expected Result : 'The lyrics is good!'
'The lyrics is poor!'
"""


def notpoor(str1):
    snot = str1.find('not')
    spoor = str1.find('poor')

    if snot < spoor and snot > 0 and spoor > 0:
        str1 = str1.replace(str1[snot:spoor+4], "good")

    return str1

print(notpoor("she is not so poor"))
