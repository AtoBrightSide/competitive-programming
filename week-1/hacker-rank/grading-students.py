def gradingStudents(grades):
    # Write your code here
    rounded_grades=[]
    for grade in grades:
        rounded_grades.append(grade) if (((grade//5)*5)+5)-grade>=3 or grade<38 else rounded_grades.append(((grade//5)*5)+5)
    return rounded_grades

gradingStudents([65,78,45,34])