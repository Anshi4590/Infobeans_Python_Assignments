'''33Find the longest word. 
S = "find the longest word"
output - 
"longest"
'''
s = input("Enter String  : ")
m = s.split(" ")
longest = m[0]
for i in m:
    if len(i)>len(longest):
        longest = i

print(f"Longest word in the sentence  : {longest}")