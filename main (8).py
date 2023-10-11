class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):
  sorted_students = sorted(student_list,
                           key=lambda student: student.cgpa,
                           reverse=True)
  return sorted_students


students = [
    Student("Sindhu", "A123", 7.8),
    Student("Swathy", "A124", 8.8),
    Student("Janani", "A125", 9.8),
    Student("Banu", "A126", 9.9)
]
sorted_students = sort_students(students)
for student in sorted_students:
  print("name:{},roll number:{},cgpa:{}".format(student.name,
                                                student.roll_number,
                                                student.cgpa))
