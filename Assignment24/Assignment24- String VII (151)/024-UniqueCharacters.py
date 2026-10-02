'''24 Check if all characters in a string are unique. 
S1 = "abc", S2 = "abca" 
 output = S1: True, S2: False'''

s = input("Enter String : ")
result = ""
for i in s:
    count = 0
   
    for j in s:
      if i == j:
         count+=1
    if count==1:
       result+=i

print(result)