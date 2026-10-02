s =input("Enter string:")
words = s.split()
for i in range(0,len(words)):
    w= words[::-1]
    for j in range(len(w)-1):
        print(" ".join(words[::-1]))