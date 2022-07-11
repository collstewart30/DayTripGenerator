def day_trip_generator(list, option):
    list_choice = iter(list)

    for destination in list:
        print(f'We have selected {list} for your {option}. Would you like to confirm?')
        user_input = input("yes or no: ")
        
        if user_input == 'yes':
            return ('Have fun in ' + destination)
        elif user_input == 'no':
            return ('Would you like to go to ' + next(list_choice) + '?')



destinations_list = ['Philadelphia', 'Baltimore', 'D.C.', 'NYC']
destination_chosen = day_trip_generator(destinations_list, 'destination')





# def semester_grades(grades, courses):
#     grades_received = len(grades)
#     grade = 0
#     while grade < grades_received:
#         print(f'This semester, i got an {grades[grade]} in {courses[grade]}')
#         grade = grade + 1


# grade_list = ["A", "B", "A+", "C", "B-"]
# course_list = ['math', 'science', 'gym', 'art', 'history']

# semester_grades(grade_list, course_list)





# restaurants_list = ['Chic Fil A', 'WaWa', "Wendy's", 'Taco Bell']
# transportation_modes_list = ['Car', 'Plane', 'Scooter', 'Train']
# entertainment_choices_list = ['Museum', 'Hike', 'Shop', 'Swim']