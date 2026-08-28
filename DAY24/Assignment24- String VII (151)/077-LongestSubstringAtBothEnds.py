
'''
77. Find the longest substring that appears at both ends. 
S = "abracadabra" 
"abra"

'''
s = input("Enter String : ")
sub = ""
long = 0

for i in range(len(s)):
    temp =""

    for j in range(i,len(s)//2):

        temp+=s[j] # a

        if s[:len(temp)] == temp and s[len(s)-len(temp):len(s)] == temp and len(temp)>long :
            sub = temp
            long = len(sub)

print(sub)