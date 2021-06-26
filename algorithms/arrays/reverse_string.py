# Given an array (or string), the task is to reverse the array/string

def reverse(string):
    gnirts = ""

    for i in range(len(string)):
        gnirts += string[len(string)-i-1]
    
    return gnirts

print(reverse("string"))