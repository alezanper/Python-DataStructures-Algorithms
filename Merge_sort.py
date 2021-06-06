import math
            
def mergeSort(uList):
    
    if(len(uList)<2):
        return uList
    middle = math.floor(len(uList)/2)
    lList = uList[0:middle]
    rList = uList[middle:]
    
    return merge(mergeSort(lList), mergeSort(rList))

def merge(leftList, rightList):
    leftIndex = 0
    rightIndex = 0
    semiOrdered = []

    while(leftIndex < len(leftList) and rightIndex < len(rightList)):
        if((leftList[leftIndex])<(rightList[rightIndex])):
            semiOrdered.append(leftList[leftIndex])
            leftIndex+=1
        else:
            semiOrdered.append(rightList[rightIndex])
            rightIndex+=1
    
    leftRemains = leftList[leftIndex:]
    rightRemains = rightList[rightIndex:]
    
    semiOrdered.extend(leftRemains)
    semiOrdered.extend(rightRemains)
        
    return semiOrdered

u_list = [71, 12, -7, 63, 4, 50, 6, 78, 0, 4, 6, 8, 9, -4]

print(mergeSort(u_list))