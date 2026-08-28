'''76 Find the longest common suffix among strings. 
Strings = ["baking", "making", "taking"] 
"king"'''

n = int(input("Enter number of words : "))
l =[]

for i in range(n):
    m = input("Enter string :")
    l.append(m)

print(l)

suffix = l[0]


for i in range(1,len(l)):
    temp = ""

    for j in range(-1,-(min(len(suffix),len(l[i]))+1),-1):
        
        if suffix[j] == l[i][j]:
           temp=suffix[j]+temp

    if len(temp)<len(suffix):
        suffix = temp

print(suffix)