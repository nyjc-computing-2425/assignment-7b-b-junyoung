import math


GRADE = {}
for score in range(0, 101):
    if score >= 70:
        GRADE[score] = 'A'
    elif score >= 60:
        GRADE[score] = 'B'
    elif score >= 55:
        GRADE[score] = 'C'
    elif score >= 50:
        GRADE[score] = 'D'
    elif score >= 45:
        GRADE[score] = 'E'
    elif score >= 40:
        GRADE[score] = 'S'
    else:
        GRADE[score] = 'U'


def read_testscores(filename):
  """
  1. Takes a string filename
  2. Reads in data from the file filename in CSV format
  3. Represents each row's data as a dict with the following keys:
      'class'
      'name'
      'overall' (Calculates the overall score of each student and stores it under the 'overall' key)
      'grade' (Determines the grade of each student and stores it under the 'grade' key)
  4. Returns a list of dicts, each dict representing row data for a single student

  Parameter
  ---------
  filename: str
    contains data on testscores

  Returns
  ---------
  student_data: list
    list of dicts, each dict representing row data for a single student
    
  Example:
  >>> studentdata = read_testscores('testscores.csv')
  >>> studentdata[0]['class']
  'Class1'
  >>> studentdata[0]['name']
  'Student1'
  >>> studentdata[0]['overall']
  51
  >>> studentdata[0]['grade']
  'D'
  """
  student_data = []

  with open(filename, 'r') as file:
      lines = file.readlines()

      for line in lines[1:]:
          data = line.strip().split(',')
          p1, p2, p3, p4 = map(int, data[2:])
          overall = math.ceil((p1 / 30 * 15) + (p2 / 40 * 30) + (p3 / 80 * 35) + (p4 / 30 * 20))
          grade = GRADE[overall]
          student = {
              'class': data[0],
              'name': data[1],
              'overall': overall,
              'grade': grade,
          }
          student_data.append(student)

  return student_data


def analyze_grades(student_data):
  """
  Takes the student data and returns a dict representing the count of each grade for each class

  Parameter
  ---------
  student_data: list
    

  Returns
  ---------
  class_grades: dict
    contains count of each grade for each class

  Example:
  >>> analysis = analyze_grades(studentdata)
  >>> analysis['Class1']['A']
  4
  >>> analysis['Class18']['U']
  0
  """

  class_grades = {}
  
  for student in student_data:
      class_name = student['class']
      grade = student['grade']
      
      if class_name not in class_grades:
          class_grades[class_name] = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'S': 0, 'U': 0}
          
      class_grades[class_name][grade] += 1
      
  return class_grades