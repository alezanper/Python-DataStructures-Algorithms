def isAnagram(a, b):

    # Preparation
    a = a.replace(" ", "")
    b = b.replace(" ", "")
    a = a.lower()
    b = b.lower()

    # edge cases
    if ((len(a)==0) or (len(b)==0)):
        return False

    if ((len(a) != len(b))):
        return False    

    # Auxiliar Variables
    dictionary = {}

    for letter in a:
        if letter in dictionary:
            dictionary[letter] +=1
        else:
            dictionary[letter] = 1

    for letter in b:
        if letter in dictionary:
            dictionary[letter] -=1
        else:
            dictionary[letter] = 1

    for k in dictionary:
        if dictionary[k] != 0:
            return False
    
    return True


def main():
    print(isAnagram('dooiig', 'gooiod'))

if __name__ == '__main__':
    main()