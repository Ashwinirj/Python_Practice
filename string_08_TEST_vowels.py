a = "ashwini"
vowels = ["a","e", "i", "o", "u", "A", "E", "I", "O", "U"]
result = ""

#Below program prints "shwn"
# for i in range(len(a)):
#     if a[i] not in vowels:
#         result = result +a[i]

# printing "ashwn"
for i in a:
    if i in vowels:
        result =  a.replace(i, "")

print(result)

