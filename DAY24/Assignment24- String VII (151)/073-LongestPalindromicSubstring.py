''' 73. Find the longest palindromic substring. S = "babad" "bab" (or "aba") '''

s = input("Enter String :")
max = ""
for i in range(len(s)):

    sub =""
    for j in range(i,len(s)):
        sub+=s[j]
        rev =""
        for k in range(-1,-len(sub)-1,-1):
            rev+=sub[k]

        if rev == sub and len(rev)>len(max):
            max = sub

print(max)