
def is_boom(phrase):
    boom = ['b', 'o', 'o', 'm']

    log = {}
    new_word = []

    for letter in phrase:
        if letter in boom:
            new_word.append(letter)

    index = 0
    is_boom = ""
    for character in new_word:
        if character == boom[index]:
            index += 1
            is_boom += character
    
    return is_boom



print(is_boom("every breath you take every move you make"))
