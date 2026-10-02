from models.student import Student
student_db = []

for i in range(2):

    rollno = int(input("Enter Roll number :"))
    name = input("Enter Name : ")
    marks = int(input("Enter marks : "))
    print()

    student = Student(rollno,name,marks)
    student_db.append(student)

# print(studentlist)

# student_db[0].display_details(student_db)
print("====== Students =========")

for s in student_db:
    s.display_details()

print()

print("Students with Marks above 60 : ")

for i in student_db:
    if i.search_marks():
        i.display_details()

print()
print("Students with Highest Marks : ")

high = student_db[0]

for i in student_db:
    if i.highest_marks(high):
        high = i

high.display_details()

print()

print("Average:")
print(Student.average(student_db))


