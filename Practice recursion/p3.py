def add(n,sum):
    if n == 0:
       return sum 
   
    sum+=n
    return add(n-1,sum)
    
 
print(add(5,0))