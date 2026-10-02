'''' 22Find the last repeating character.
 S = "abracadabra" 
 output = r'''
s = input("Enter String : ")
last = ""
for i in s:
    count = 0
    for j in s:
        if i == j:
           count+=1
           last = i
    
print(last)
   
