'''
78 Find the longest mirror-image substring at both ends. 

S = "aabccbaa"

"aab" 

'''
s = input("Enter String : ")
sub = ""
long = 0

for i in range(len(s)):
    temp =""

    for j in range(i,len(s)//2):

        temp+=s[j] # a

        if s[:len(temp)] == temp and s[len(s)-len(temp):len(s)] == temp[::-1] and len(temp)>long :
            sub = temp
            long = len(sub)

print(sub)