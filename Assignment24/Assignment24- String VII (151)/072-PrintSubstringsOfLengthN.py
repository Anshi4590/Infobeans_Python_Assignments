'''
72.Print all substrings of length n. 
S = "abc", 
n = 2 
"ab, bc"

'''


s = input("Enter String : ")
n = int(input("Enter length: "))

for i in range(0,len(s)):
    sub =""
    sub = s[i]
    if n==1:
      print(s[i] , end = ",")

    for j in range(i+1,len(s)):

        sub+=s[j]
        if n == len(sub):  
           print(sub , end = " ")



# more simplified version 


for i in range(0, len(s) - n + 1):
    sub = ""

    for j in range(i, i + n):
        sub += s[j]

    print(sub, end=" ")