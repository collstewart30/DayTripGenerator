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


destinations = ['Philadelphia', 'Baltimore', 'D.C.', 'NYC']
restaurants = ['Italian', 'Mexican', 'Thai', 'American']
transportation_modes = ['car', 'plane', 'scooter', 'train']
entertainment_choices = ['Museum', 'Hike', 'Shop', 'Game']



import random

destination_confirmed = False

while (destination_confirmed == False):
    print('Would you like to go to ' + random.choice(destinations) + '?')    
    user_types = input("yes or no: ")

    if (user_types == 'yes'):
        destination_confirmed = True
        print("Congrats on your destination!")
    else:
        print('Please try again.')

# how to make it not repeat cities

restaurant_confirmed = False

while (restaurant_confirmed == False):
    print('Would you like to go to ' + random.choice(restaurants) + '?')    
    user_types = input("yes or no: ")

    if (user_types == 'yes'):
        restaurant_confirmed = True
        print("Congrats on your restuarant!")
    else:
        print('Please try again.')



transportation_confirmed = False

while (transportation_confirmed == False):
    print('Would you like to go by ' + random.choice(transportation_modes) + '?')    
    user_types = input("yes or no: ")

    if (user_types == 'yes'):
        transportation_confirmed = True
        print("Congrats on your transportation!")
    else:
        print('Please try again.')


entertainment_confirmed = False

while (entertainment_confirmed == False):
    print('Would you like to go to a ' + random.choice(entertainment_choices) + '?')    
    user_types = input("yes or no: ")

    if (user_types == 'yes'):
        entertainment_confirmed = True
        print("Congrats on your entertainment!")
    else:
        print('Please try again.')