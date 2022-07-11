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




# how to make random not repeat what it's already listed?
# maybe a sequence type call?

# some_list = ['a', 'b', 'c', 'd', 'e', 'f']
# random_iterator = iter(some_list)
# print(next(random_iterator)) #Output = a
# print(next(random_iterator)) #Output = b


# random_iterator2 = iter(destinations)

# print('Would you like to go to ' + next(random_iterator2) + '? Type yes or no. ')
# print('Would you like to go to ' + next(random_iterator2) + '? Type yes or no. ') 
# print('Would you like to go to ' + next(random_iterator2) + '? Type yes or no. ')
# print('Would you like to go to ' + next(random_iterator2) + '? Type yes or no. ') 




destinations = ['Philadelphia', 'Baltimore', 'D.C.', 'NYC']
restaurants = ['Italian', 'Mexican', 'Thai', 'American']
transportation_modes = ['car', 'plane', 'scooter', 'train']
entertainment_choices = ['Museum', 'Hike', 'Shop', 'Game']

import random
from stat import FILE_ATTRIBUTE_SPARSE_FILE


# trip_confirmed = False

# while trip_confirmed == False:






destination_confirmed = False
destination_iterator = iter(destinations)
choice_number = 1

# what to do when user denies all options in list?

while destination_confirmed == False:
        
    print('Would you like to go to ' + next(destination_iterator) + '? Type yes or no. ') 
    user_types = input("yes or no: ")

#    if user_types != ('yes') or ('no'):        # want something here for a user input typo
#       print('I did not recognize that. Please try again.')
#       destination_confirmed = False           # how to get iteration to start from correct point/repeat index instead of next iteration
    
    
    
    if (user_types == 'no') and choice_number == 4:
        print('Your randomly selected destination is: ' + random.choice(destinations))
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
        print('Congrats on your destination!')
    else:
        print('not sure')
        



# restaurant_confirmed = False
# restaurant_iterator = iter(restaurants)

# while restaurant_confirmed == False:
        
#     print('Would you like to go to ' + next(restaurant_iterator) + '? Type yes or no. ') 
#     user_types = input("yes or no: ")

#     if (user_types == 'no'):
#         restaurant_confirmed = False
#     else:
#         restaurant_confirmed = True
#         print('Congrats on your restaurant!')


# transportation_confirmed = False
# transportation_iterator = iter(transportation_modes)

# while transportation_confirmed == False:
        
#     print('Would you like to go take a ' + next(transportation_iterator) + '? Type yes or no. ') 
#     user_types = input("yes or no: ")

#     if (user_types == 'no'):
#         transportation_confirmed = False
#     else:
#         transportation_confirmed = True
#         print('Congrats on your transportation!')

    
# entertainment_confirmed = False
# entertainment_iterator = iter(entertainment_choices)

# while entertainment_confirmed == False:
        
#     print('Would you like to go to a ' + next(entertainment_iterator) + '? Type yes or no. ') 
#     user_types = input("yes or no: ")

#     if (user_types == 'no'):
#         entertainment_confirmed = False
#     else:
#         entertainment_confirmed = True
#         print('Congrats on your entertainment!')