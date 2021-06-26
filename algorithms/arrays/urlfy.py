# write a method to replace all spaces in a string with %20 
# input: "Mr John Smith     ", 13
# output: ""Mr%20John%20Smith"

def add20(string):
    string2 = string.strip() 
    string3 = ""

    for character in string2:
        if character == " ":
            string3 += "%20"
        else:
            string3 += character
    return string3

print(add20("    hello world   "))