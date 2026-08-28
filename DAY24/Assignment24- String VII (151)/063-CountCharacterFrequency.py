'''
63 Count frequency of each character. 
S = "aabcc" 
a: 2, b: 1, c: 2'''

s = input("Enter String:")

m =""
for i in s:
    count =0
    if i not in m:
        for j in s:
            if i==j:
                count+=1
        m+=i
        print(f"{i}: {count}")

# we use count in this
n=""
for i in s:
    if i not in n: 
        m = s.count(i)
        print(f"{i}: {m}")

        n+=i