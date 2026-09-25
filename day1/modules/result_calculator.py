

# TODO
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
   