'''27 Find the last occurrence of a word. S = "Test this test", Word = "test" 15 (index)'''

m = input("Enter String : ")
word = input("Enter word : ")

for i in range(len(m)-len(word),len(word)-1,-1):
    if m[i:i+len(word)] == word:
        print(f"The last occurence of the word is {i} ")
        break
