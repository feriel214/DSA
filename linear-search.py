#Linear_search
def linear_search(list,target):
    for i in range(0, len(list)):
        if list[i] == target:
            return i
       
    return -1
    
def verify(index):
    if index == -1:
        print('target not found in the list ')
    else:
        print("target found at index: ",index)    
numbers = [1,2,3,4,5,6]
verify(linear_search(numbers,6))