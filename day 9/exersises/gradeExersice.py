student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades ={}

for key in student_scores:
    if 100 >= student_scores[key] >= 91:
        student_grades[key] = "Outstanding"
    elif 90 >= student_scores[key] >= 81:
        student_grades[key] = "Exceeds Expectations"
    elif 80 >= student_scores[key] >= 71:
        student_grades[key] = "Acceptable"
    else: 
        student_grades[key] = "Fail"


for key in student_grades:
    print(key, student_grades[key])