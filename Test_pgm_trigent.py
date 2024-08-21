import re
def LongestWord(sen):

  # code goes here
 # Remove punctuation from the string
    cleaned_sen = re.sub(r'[^\w\s]', '', sen)
    
    # Split the cleaned string into words
    words = cleaned_sen.split()
    
    # Initialize variables to find the longest word
    varOcg = ""
    max_length = 0
    
    # Iterate through each word to determine the longest one
    for word in words:
        if len(word) > max_length:
            varOcg = word
            max_length = len(word)
    
    # Return the longest word found
    return varOcg

# keep this function call here 
print(LongestWord(input()))