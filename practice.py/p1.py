line_count = 0
word_count = 0
with open ("file.txt","r") as f:

    for line in f:

        line_count+=1
        word_count+=len(line.split())

print(line_count)
print(word_count)