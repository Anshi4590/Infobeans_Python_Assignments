'''
75 Find the longest common prefix among strings. Strings = ["flower", "flow", "flight"] 
output:
"fl"

'''

n = int(input("Enter number of words : "))
l =[]

for i in range(n):
    m = input("Enter string :")
    l.append(m)

print(l)

preffix = l[0]
sub = ""

for i in range(1,len(l)):
    temp = ""

    for j in range(min(len(preffix),len(l[i]))):
        
        if preffix[j] == l[i][j]:
           temp+=preffix[j]

    if len(temp)<len(preffix):
        preffix = temp

print(preffix)