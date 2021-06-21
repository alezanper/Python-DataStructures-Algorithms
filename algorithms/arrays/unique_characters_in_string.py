# Given a string, determine if it is compreised of all unique characters. 
# "abcde" returns true
# "aabcde" returns false

def unique_characters(text):
    dictionary = {}
    for letter in text:
        if letter not in dictionary:
            dictionary[letter] = 1
        else:
            dictionary[letter] += 1
    
    for key in dictionary.keys():
        if(dictionary[key] > 1):
            return False
    return True

print(unique_characters("aabcde"))   # False
print(unique_characters("abcdef"))   # True