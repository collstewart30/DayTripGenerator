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



destinations_list = ['Philadelphia', 'Baltimore', 'D.C.', 'N.Y.C.', 'Annapolis', 'Boston', 'Chicago']
restaurants_list = ['Chic Fil A', 'WaWa', "Wendy's", 'Taco Bell', "Raising Cane's", 'Shake Shack', "Arby's"]
transportation_modes_list = ['car', 'plane', 'scooter', 'train', 'motorcycle', 'helicopter', 'boat']
entertainment_choices_list = ['going to a museum', 'going on a hike', 'shopping', 'swimming', 'sightseeing', 'seeing a movie', 'going to the zoo']

import random

def random_generator(list):
    random_item = random.choice(list)
    return random_item


def user_destination_confirmation():
    user_confirmed = False
    while user_confirmed == False:
        random_destination = random_generator(destinations_list)
        user_input = input(f'How about {random_destination} as your destination? y/n ')
        if user_input == 'y':
            print(f'Thanks for choosing {random_destination}!')
            return random_destination
        else:
            print('Pick again!')


def user_restaurant_confirmation():
    user_confirmed = False
    while user_confirmed == False:
        random_restaurant = random_generator(restaurants_list)
        user_input = input(f'Would you like to eat at {random_restaurant}? y/n ')
        if user_input == 'y':
            print(f'Thanks for choosing {random_restaurant}!')
            return random_restaurant
        else:
            print('Pick again!')


def user_transportation_confirmation():
    user_confirmed = False
    while user_confirmed == False:
        random_transportation = random_generator(transportation_modes_list)
        user_input = input(f'Would you like to get around by {random_transportation}? y/n ')
        if user_input == 'y':
            print(f'Thanks for choosing {random_transportation}!')
            return random_transportation
        else:
            print('Pick again!')


def user_entertainment_confirmation():
    user_confirmed = False
    while user_confirmed == False:
        random_entertainment = random_generator(entertainment_choices_list)
        user_input = input(f'Would you enjoy {random_entertainment} as your activity? y/n ')
        if user_input == 'y':
            print(f'Thanks for choosing {random_entertainment}!')
            return random_entertainment
        else:
            print('Pick again!')


def day_trip_generator():
    destination_selection = user_destination_confirmation()
    restaurant_selection = user_restaurant_confirmation()
    transportation_selection = user_transportation_confirmation()
    entertainment_selection = user_entertainment_confirmation()
    print(f'Thank you for your selections! Your trip is as follows: destination: {destination_selection}, restuarant: {restaurant_selection},transportation: {transportation_selection}, and entertainment: {entertainment_selection}.')
    
def day_trip_confirmed():
    user_confirm_trip = input('Do you want to confirm? y/n ')  
    if user_confirm_trip == 'y':
        print('Congrats! Your trip is confirmed!')
    else:
        day_trip_generator()


day_trip_generator()
day_trip_confirmed()