'''5.

=========================================
WORD LENGTH GROUPING
====================

A content management system stores article tags.

tags = ["python","java","api","react","html","css"]

Write a program to:

* Group words according to their length.
* Store result in dictionary.

Sample Output:
{
3:['api','css'],
4:['java','html'],
5:['react'],
6:['python']
}

'''

tags = list(input("Enter Tags :").split())

d = {}

for i in tags :

    length = len(i)

    if length not in d:
        d[length] = []

    d[length].append(i)

print(d)

d = dict(sorted(d.items()))
print(d)