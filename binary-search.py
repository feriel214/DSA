#binary search algorithm 
def binary_search(list,target):
    first = 0
    last = len(list)- 1
    while first <= last:
        midpoint=(first+last)//2
        if list[midpoint]==target :
            return midpoint
        elif list[midpoint]<target :
             first=midpoint+1
        else:
            last = midpoint- 1 
    return -1

def verify(index):
    if index == -1 :
        print('The target is not in the list ')  
    else :
        print('The target is found at position : ',index+1)  

numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]  
verify(binary_search(numbers,1))                       


