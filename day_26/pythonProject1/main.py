import random
# names = ["Alex", "Beth", "Aiden", "Kai", "Chan", "Angela"]
#
# student_scores = {student: random.randint(0,100) for student in names}
# print(student_scores)
#
# passed_students = {student: mark for student,mark in student_scores.items() if mark>60 }
#
# print(passed_students)

student_dict = {
    "student":  ["Alex", "Beth", "Aiden", "Kai", "Chan", "Angela"],
    "score" : [2,37,65,73,23,98]
}
import pandas

student_df = pandas.DataFrame(student_dict)

for (index, row) in student_df.iterrows():
    print(row.score)