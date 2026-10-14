student_list = {
    "Ed" : "A",
    "Edd" : "B",
    "Eddy" : "F"
}

grade = input("Please type a student name : ")

if grade in student_list
    print(student_list.get(grade))
else :
    print("Student not found")