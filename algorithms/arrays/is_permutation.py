# given two strings write a method to decide if one is a permutation of the other
# For example, “abcd” and “dabc” are Permutation of each other.

def is_permutation(string1, string2):

    d = {}

    if (len(string1)!=(len(string2))):
        return False

    for i in range(len(string1)):
        if string1[i] in d:
            d[string1[i]] += 1
        else:
            d[string1[i]] = 1
    
    for i in range(len(string2)):
        if string2[i] in d:
            d[string1[i]] -= 1
        else:
            d[string1[i]] = 1

    for j in d.values():
        if j > 0:
            return False

    return True

print(is_permutation("hello", "lloeh"))
print(is_permutation("world", "lloeh"))