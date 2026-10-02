'''34Find the shortest word. 
S = "find the shortest word" 
output -
"the" '''

s = input("Enter String  : ")
m = s.split(" ")
shortest = m[0]
for i in m:
    if len(i)<len(shortest):
       shortest = i
print(f"Shortest word in the sentence  : {shortest}")