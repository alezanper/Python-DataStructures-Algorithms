# Given a nested list return the elements on a list
# ['a','b','c',['d','e', ['f', 'g'],'h']]   ->   ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']   
def recursive_approach(l:list):
    final = []
    for element in l:
        if len(element) == 1:
            final.append(element)
        else:
            final.extend(recursive_approach(element))

    return final

l = ['a','b','c',['d','e', ['f', 'g'],'h']]
print(recursive_approach(l))