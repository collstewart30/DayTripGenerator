def semester_grades(grades, courses):
    grades_received = len(grades)
    grade = 0
    while grade < grades_received:
        print(f'This semester, i got an {grades[grade]} in {courses[grade]}')
        grade = grade + 1


grade_list = ["A", "B", "A+", "C", "B-"]
course_list = ['math', 'science', 'gym', 'art', 'history']

semester_grades(grade_list, course_list)