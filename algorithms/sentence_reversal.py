# Given a string of words, reverse all the words
# Given "this is the best"  -> "best the is this"

def rev_word(phrase):
    words = phrase.split()
    sdrow = ""
    
    k = len(words)
    for i in range(k):
        sdrow += words[k-i-1] + " "
    print(sdrow)


rev_word("this is the best")