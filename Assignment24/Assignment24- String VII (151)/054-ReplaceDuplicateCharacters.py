'''54 Replace all duplicate characters with '$'. 
S = "hello" 

output:

"he$lo"
'''

s = input("Enter String : ")
n=s
unique =""
for i in range(len(s)):
    count =0
    for j in range(i+1,len(s)):
        if s[i] == s[j]:
           count+=1
        
    if count == 1:
        unique+="$"
    else:
        unique+=s[i]
print(unique)

# or if you want to replace duplicate elements with "$"

# using method

for i in n:
    if n.count(i)>1:
       n= n.replace(i,"$")
print(n)
