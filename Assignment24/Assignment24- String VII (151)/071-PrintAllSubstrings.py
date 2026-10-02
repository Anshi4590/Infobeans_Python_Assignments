'''
71. Print all substrings. 
S = "abc" 

"a, b, c, ab, bc, abc" 

'''
s = input("Enter String : ")

for i in range(0,len(s)):
    print(s[i] , end = ",")
    sub = s[i]

    for j in range(i+1,len(s)):
        sub+=s[j]
        print(sub , end = ",")


# more simplified 

for i in range(0,len(s)):
    
    sub =""

    for j in range(i, len(s)):

        sub+=s[j]
        print(sub , end = ",")




