'''67 Count how many times a substring appears. 
S = "abab", 
Sub = "ab"'''

s = input("Enter String : ")
sub = input("Enter Substring :")

count = 0

for i in range(0,len(s)-len(sub)+1):

    if s[i:i+len(sub)]== sub:
        count+=1

print(count)



