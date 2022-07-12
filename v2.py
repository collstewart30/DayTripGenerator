# (5 points): As a developer, I want to make at least three commits with descriptive messages.
# (5 points): As a developer, I want to store my destinations, restaurants, mode of transportations, and entertainments in their own separate lists.
# (5 points): As a user, I want a destination to be randomly selected for my day trip.
# (5 points): As a user, I want a restaurant to be randomly selected for my day trip.
# (5 points): As a user, I want a mode of transportation to be randomly selected for my day trip.
# (5 points): As a user, I want a form of entertainment to be randomly selected for my day trip.
# (15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things.
# (10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections.
# (10 points): As a user, I want to display my completed trip in the console.
# (5 points): As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing!

import random
from stat import FILE_ATTRIBUTE_SPARSE_FILE

restaurants_list = ['Chic Fil A', 'WaWa', "Wendy's", 'Taco Bell']
transportation_modes_list = ['Car', 'Plane', 'Scooter', 'Train']
entertainment_choices_list = ['Museum', 'Hike', 'Shop', 'Swim']


def destination_choice_won(destination_list):


        destination_confirmed = False
        destination_choice = iter(destinations_list)
        choice_number = 1


        for city in destinations_list:
                   
            print('Would you like to go to ' + next(destination_choice) + '?')
            user_types = input("yes or no: ")
        
                    
            if (user_types == 'no') and choice_number == 4:
                random_selection_dest = ('Your randomly selected destination is: ' + (random.choice(destinations_list)))
                print(random_selection_dest)
                break
            elif (user_types == 'no') and choice_number < 3:
                choice_number += 1
                destination_confirmed = False
            elif (user_types == 'no') and choice_number == 3:
                print("")
                print('Last choice!')
                print("")
                destination_confirmed = False
                choice_number += 1
            elif (user_types == 'yes'):
                destination_confirmed = True
                print("")
                print('Congrats on your destination!')
                return destination_choice
            else:
                print('Please try again.')


destinations_list = ['Philadelphia', 'Baltimore', 'D.C.', 'NYC']
destination_choice = destination_choice_won (destinations_list)

print(destination_choice)


