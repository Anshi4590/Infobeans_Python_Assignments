def pow(a,b):
    if b ==1:
        return a
        
    result = a*pow(a,b-1)
    return result 
    
print(pow(3,2))