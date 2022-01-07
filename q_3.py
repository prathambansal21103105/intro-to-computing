#question 3:make a list of SID,NAME,GENDER,COURSE NAME,CGPA
#answer: source code

name=input("Please enter name: ")
sid= input("Enter student Id: ")
gender=input("Enter gender: ")
course_name=input("Enter your course name: ")
cgpa=input("Enter cgpa: ")
sid=int(sid)
cgpa=float(cgpa)
#our list now name as student_info
data=['Name','SID','Gender','Course name','Cgpa']
print(data)
student_info=[name,sid,gender,course_name,cgpa]
print(student_info)
