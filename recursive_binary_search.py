 #recursive binary search 
def recursive_binary_search(list,target):
    if len(list)==0: 
        return False
    else :
     midpoint=(len(list))//2
    if midpoint == target:
        return True 
    else : 
        if list[midpoint] < target:
            return recursive_binary_search(list[midpoint+1:],target)  
        else: 
            return recursive_binary_search(list[:midpoint],target) 


def verify(res):
    if  res :
        print(' Traget found in the list ')
    else : 
         print(' Traget not found in the list ')
numbers=[1,2,3,4,5,6,7,8,9,10]
verify(recursive_binary_search(numbers,1157))
verify(recursive_binary_search(numbers,5))
