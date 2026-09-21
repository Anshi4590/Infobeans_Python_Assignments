def pow(a,b):
    if b==0:
        
        return 1
        
    if b%2 == 0:
       ans = pow(a,b//2)*pow(a,b//2)
       
    else:
        
       ans  = pow(a,b//2)*pow(a,b//2)*a
    return ans
        
print(pow(3,3))