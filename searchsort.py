
class student:
    def __init__(self, name, studentId, gpa, credits):
        self.name = name
        self.bannerId = studentId
        self.gpa = gpa
        self.credits = credits


    def __str__(self):
        return f"Student with name: {self.name} and bannerID: {self.bannerId} \n gpa: {self.gpa}, credits: {self.credits}"
#end student class

def binary_search(list_of_students, student_to_find):
    if list_of_students ==[]:
        return None
    middle = len(list_of_students)//2
    middlestudent = list_of_students[middle]
    if middlestudent.name == student_to_find:
        return middlestudent
    if middlestudent.name < student_to_find:
        return binary_search(list_of_students[middle+1:], student_to_find)
    else:
        return binary_search(list_of_students[:middle-1], student_to_find)

def get_data(filename):
    student_file = open(filename)
    lines = student_file.readlines()
    list_of_students = []
    for student_line in lines:
        data = student_line.split('|')
        current_student = student(data[0], int(data[1]), gpa=float(data[3]), credits=int(data[2]))
        list_of_students.append(current_student)
    return list_of_students

def get_key(student_to_sort):
    return student_to_sort.gpa

def main():
    student_data = get_data("students.txt")
    student_data.sort(key=get_key)
    stu_to_find = input("what student should we find")
    result = binary_search(student_data, stu_to_find)
    print(result)
  #  for stu in student_data:
   #     print(stu)

main()