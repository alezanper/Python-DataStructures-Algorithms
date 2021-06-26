# Given a string, write a function to check if it is a permutation of a palindrome.
# example:
# input: Tact Coa
# output True (permutations: "taco cat", "atco cta")

def palindrome_permutation(string):

    string = string.lower()
    dictionary = {}
    ones = 0

    for character in string:
        if character == " ":
            continue
        if character in dictionary:
            dictionary[character] += 1
        else:
            dictionary[character] = 1

    for count in dictionary.values():
        if count % 2 != 0 and count != 1:
            return False
        if count == 1:
            ones += 1
    
    if ones > 1:
        return False

    return True        

print(palindrome_permutation("Tact Coa"))
print(palindrome_permutation("Tact Coas"))
print(palindrome_permutation("lllla"))