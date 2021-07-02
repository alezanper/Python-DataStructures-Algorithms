# Implement an algorithm to determine if a string has all unique characters. What if you cannot use 
# additional data structures

def is_unique(string):

    seen = set()
    for i in range(len(string)):
        if (string[i] not in seen):
            seen.add(string[i])
        else:
            return False

    return True

print(is_unique("Hello"))
print(is_unique("world"))