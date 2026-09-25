# Day 1 - Python Fundamentals
def input_student():
  student_name = input("Enter student name:")
  marks_python = float(input("Enter marks for Python:"))
  marks_math = float(input("Enter marks for Mathematics:"))
  marks_comm = float(input("Enter marks for Communication:"))
  dict_student_info = {
    "name":student_name,
    "python_marks":marks_python,
    "math_marks":marks_math,
    "comm_marks":marks_comm
  }
  # return student_name,marks_python,marks_math,marks_com
  return dict_student_info

def calculate_percentage(marks_python,marks_math,marks_comm):
 total=(marks_python+marks_math+marks_comm)
 percentage = (total/300)*100
 return percentage


# percentage = 0
if __name__ =="__main__":
 print("\n -- Result --")
 student_info=input_student()
 #name,python_m,comm_m=input_student()
 print(student_info)

 
 print("student", student_info["name"])
 print("percentage",calculate_percentage(
       student_info["python_marks"],
       student_info["math_marks"],
       student_info["comm_marks"]
 ))
