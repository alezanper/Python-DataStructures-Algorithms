# Given a string "AAAABBBBCCCCCDDEEEE" returns "A4B4C5D2E4"
# Case sensitive 
# "AAB" returs "A2B1"

def string_compression(text):
    dictionary = {}
    compress = ""
    for letter in text:
        if letter not in dictionary:
            dictionary[letter] = 1
        else:
            dictionary[letter] += 1
    
    for key in dictionary.keys():
        compress += key + str(dictionary[key])
    return compress

print(string_compression("AAAABBBBCCCCCDDEEEE"))   # A4B4C5D2E4