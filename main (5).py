class student:
  def __init__ (self,name,roll_number,cgpa): 
   self.name=Name
   self.roll_number = roll_number
   self.cpga = cpga
def sort_student(student_list):
  sorted_students=sorted(student_list, key=lambda_student:student.cgpa,reverse=True)
 return sorted_students
students=[
  student ("Sindhu","A123",7.8)
  student ("Swathy","A124",8.8)
  student ("Janani","A125",9.8)
  student ("banu","A126",9.9), 
]
sorted_student=sort_students (students) 
for student=sort_students:
 print("name:{},Roll number:{},CGPA:{}".format(student.name, student.rollnumber, student.cgpa)) 
 
