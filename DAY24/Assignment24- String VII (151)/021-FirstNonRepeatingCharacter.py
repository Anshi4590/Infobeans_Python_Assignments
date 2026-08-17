'''21Find the first non-repeating character. 
  S = "aabbcde" 
  output = c'''

s = input("Enter String : ")
for i in s:
    count = 0
    for j in s:
        if i == j:
           count+=1
    if count == 1:
       print(i)
       break
    else:
       continue
   