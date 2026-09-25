from modules.result_calculator import calculate_percentage


student_name = input("Enter student name: ")

marks_python = float(input("Enter Python marks: "))
marks_math = float(input("Enter Mathematics marks: "))
marks_comm = float(input("Enter Communication marks: "))

# TODO:
def calculate_percentage(marks_python,marks_math,marks_comm):
 total=(marks_python+marks_math+marks_comm)
 percentage = (total/300)*100
 return percentage

def calculate_grade(percentage): 
  if percentage>=80:
    grade="A"
  elif percentage>=60:
    grade="B"
  elif percentage>=40:
    grade="C"
  else:
   grade="D"

   return grade
   

# TODO:
# Calculate the percentage using the imported function

percentage = 0
print("\n--- Result ---")
print(f"Student: {student_name}")
print(f"Percentage: {percentage}")
