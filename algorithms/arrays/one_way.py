# There are three types of edits that can be performed on strings:
# insert, remove or replace a character
# pale, ple -> true +1
# pales, pale -> true +1
# pale, bake -> false +4

def one_way(string_1, string_2):

    dictionary = {}
    sum = 0

    for character in string_1:
        if character in dictionary:
            dictionary[character] += 1
        else:
            dictionary[character] = 1

    for character in string_2:
        if character in dictionary:
            dictionary[character] -= 1
        else:
            dictionary[character] = 1
    
    for value in dictionary.values():
        sum += abs(value)

    if sum > 1:
        return False

    return True 

print(one_way("pale","ple"))
print(one_way("pale","bake"))
print(one_way("pale","ba"))
print(one_way("pale","pales"))

