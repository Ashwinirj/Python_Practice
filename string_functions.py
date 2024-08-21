# len()
# str()
#

S1 = "Morning Ashwini"
#print(len(S1))

# num = 105467829101 
# num2 = str(num)
# print(num2.find('29'))

# print(S1.upper())
# print(S1.lower())
# print(S1.count('i'))
# # count(sub_string, starting_index, ending_index)
# print(S1.count("A",0,10))
# # isupper() and islower()
# print(S1.isupper())
# print(S1.islower())

##################################################

S1 = "Morning Ashwini hi hello ash ash ash ash "
#print(len(S1))
# S1.upper()
# print(S1)
# print(S1.islower())
# print(S1.isupper())

#------------------------------------------
S = "000000 '',;; Ash like you Ash like you Ash like you   ; ' ;;; / 88888"
#print(S.split("'"))
#print(S.rsplit(";"))
#print(S.strip("'0"))

#================================================================================
# STRING SLICING 
S = "I am learning new python tricks"
#s[i:j] slice the string s from i to j, but exclude j
#s[i:j:k] slice the string s from i to j with step k
# print(S[0:10]) 
# print(S[4:8]) # lea
# print(S[-1])  #s 
# print(S[-5:])  #ricks
# print(S[-1:])  #s 

#Printing string in many ways 
# print(S)
# print(S[:])
# print(S[0:])
# print(S[::])
# print(S[::1])


# Printing stings in reverse order
# print(S[::-1])

#comma separated input
text = 'name,age,salary,place'
# print(text.index(','))

# STRING Formatting in python 

a = "Ashwini"
b = "Jadhav"

print("I am " + a + " and my last name is " + b)
print("I am %s and my last name is %s " %(a,b))
print("I am {0} and my last name is {1}".format(a,b))



