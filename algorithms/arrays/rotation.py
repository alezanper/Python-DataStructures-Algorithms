# A left rotation operation on an array shifts each of the array's elements  unit to the left. For example, if  left rotations are performed on array , then the array would become . Note that the lowest index item moves to the highest index in a rotation. This is called a circular array

def rotLeft(a, d):
    # Write your code here
    k = len(a)
    new_array = a.copy()
    
    for i in range(k):
        new_index = i - d
        
        if new_index < 0 :
            new_index = new_index + k 
        
        new_array[new_index] = a[i]
        
    return new_array
