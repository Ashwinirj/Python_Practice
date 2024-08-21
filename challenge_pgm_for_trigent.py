import re
def LongestWord(sen):

  # code goes here
    new_sen = re.sub(r'[^\w\s]', '', sen)
    print(new_sen)
    # words = new_sen.split()
    # varOcg = ""
    # max_length = 0

    # for word in words:
    #     if len(word) > max_length:
    #         varOcg = word
    #         max_length = len(word)
    # return varOcg

# keep this function call here 
print(LongestWord(input()))
# final_output = LongestWord(input())
# reverse_output= final_output[::-1]
# token = "hpknd30jw6c"
# new_token = token[::-1]
# print(reverse_output + ":" + new_token)