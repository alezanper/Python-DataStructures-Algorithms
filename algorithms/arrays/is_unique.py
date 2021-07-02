# Implement an algorithm to determine if a string has all unique characters. What if you cannot use 
# additional data structures

def is_unique(string):
    d = {}
    for i in range(len(string)):
        if (string[i] in d):
            d[string[i]] += 1
        else:
            d[string[i]] = 1
    
    for j in d.values():
        if j > 1:
            return False
    return True

print(is_unique("Hello"))
print(is_unique("world"))

