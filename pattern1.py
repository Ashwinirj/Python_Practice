#Patter1 
# for i in range(4):
#     for j in range(4):
#         print("#",end=" ")
#     print()

#Pattern2 

# for i in range(4):
#     for j in range(i+1):   #i value is incremented 
#         print("#",end=" ")
#     print()

#Pattern 3

for i in range(4):
    for j in range(4-i):  # range is reduced till i
        print("#",end=" ")
    print()