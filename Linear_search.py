def linearSearch(some_list, n):
    for item in some_list:
        #print(item)
        if(item==n):
            return True
    return False

u_list = [2,4,1,6,3,1,6,-1,9,-3,9,0,15]
print(linearSearch(u_list, 1))

u_list = [2,4,1,6,3,1,6,-1,9,-3,9,0,15]
print(linearSearch(u_list, -9))