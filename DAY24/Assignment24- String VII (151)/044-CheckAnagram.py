'''44 Check if two strings are anagrams. 
S1 = "listen", S2 = "silent" 
output - TRUE'''

s1 = input("Enter String : ")
s2 = input("Enter String : ")

if len(s1) == len(s2):
    flag = 0
    for i in s1:
        if s1.count(i)!=s2.count(i):
            flag = 1
            break
    if flag == 0:
       print("Anagram")
    else:
       print("Anagram")
else:
    print("Not a Anagram")