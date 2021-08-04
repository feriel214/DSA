#recursion 
#Factorielle 
'''4!=4*3*2*1 
   n!=(n-1)*(n-2)*...1'''
def fact(n):
    if n<= 1 :
        return 1
    else : 
        return n*fact(n-1)    

print('0!=',fact(0),'1!=',fact(1),'3!=',fact(3),'4!=',fact(4))  

#Fibonacci sequence 
'''Fn=Fn-1+Fn-2'''
def fibonaaci_sequence(n):
    if n<3: 
        return 1
    else:   
        return fibonaaci_sequence(n-1)+fibonaaci_sequence(n-2) 

print(fibonaaci_sequence(1))
print(fibonaaci_sequence(4))
print(fibonaaci_sequence(3))       