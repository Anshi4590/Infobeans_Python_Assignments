'''
57. Merge two strings alternatively (char by char). 
S1 = "ABC", 
S2 = "def" 
output:
"AdBeCf"

'''

# s1 = input("Enter String : ")
# s2 = input("Enter String : ")
# new = ""
# mini = min(len(s1),len(s2))

# for i in range(mini):
#     new+=s1[i]+s2[i]

# diff = abs(len(s2)- len(s1))

# if i != len(s1)-1:
#     new += s1[i:]
# if i != len(s2)-1:
#     new += s2[i:]

# print(new)

s1 = input("Enter String : ")
s2 = input("Enter String : ")
ans = ""
i = 0
j = 0
while i < len(s1) and j < len(s2):
    ans += s1[i]
    ans += s2[j]
    i+=1
    j+=1

if i < len(s1):
    while i < len(s1):
        ans += s1[i]
        i+=1
        
if j < len(s2):
    while j < len(s2):
            ans += s2[j]
            j+=1
print(ans)