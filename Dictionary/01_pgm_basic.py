marks = { "Ash" : 80,
         "deepak": 90,
         "Gita": 85,
         "Nivu" : 100,
         (1,2): 100,
          10:100,
           1: 200}
            # [1,2] : "hi" }  # wrong Key used here: list

# Dict_keys can be integers, strings, tuples which are immutable, Lists are not the mutable


# print(marks)
# print(marks.keys())

# print(marks.values())
# print(marks["Ash"])


# print(marks.update({"nivu": "new_nivu","navya": "[1,2,3,4,5]"}))
# print(marks)

#difference between marks.get("key") and marks["key"]

# print(marks.get("Ash"))  # this method get will return the value of key, if not found then will return NONE
# print(marks["Ash"])  # this will return value if not found then will give KeyError 

print(marks)
#print(marks.popitem()) # will return (key,value) pair, if not found will give KeyError
# print(marks.pop("Ash","Not found"))  #will return value of key that is being deleted/popped out, if not found will give KeyError
# print(marks)