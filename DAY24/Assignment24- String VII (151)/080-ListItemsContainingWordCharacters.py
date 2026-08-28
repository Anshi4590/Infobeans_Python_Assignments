'''

80.Print list items containing all characters of a given word. 

List = ["apple", "plea"], 

Word = "pal" "apple", "plea"

'''

arr = list(input("Enter Word :").split(" "))
word = input("Enter word : ")

print(arr)

for i in range(len(arr)):
    count = 0

    for j in word:
        if j in arr[i]:
           count+=1

    if count == len(word):
        print(arr[i],end = ",")

