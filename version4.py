destinations_list = ['Philadelphia', 'Baltimore', 'D.C.', 'NYC', 'Annapolis', 'Boston', 'Chicago']
restaurants_list = ['Chic Fil A', 'WaWa', "Wendy's", 'Taco Bell', "Raising Cane's", 'Shake Shack', "Arby's"]
transportation_modes_list = ['car', 'plane', 'scooter', 'train', 'motorcycle', 'helicopter', 'boat']
entertainment_choices_list = ['go to a museum', 'go on a hike', 'shop', 'swim', 'sightsee', 'see a movie', 'go to the zoo']

import random

def random_item_picker(list):
    random_item = random.choice(list)
    return random_item


def user_destination_confirmation():
    user_confirmed = False
    while user_confirmed == False:
        random_destination = random_item_picker(destinations_list)
        user_input = input(f'Would you like to keep {random_destination} as your selected destination? y/n ')
        if user_input == 'y':
            print(f'Thanks for choosing {random_destination}')
            return random_destination
        else:
            print('another option will be generated for you!')


def user_restaurant_confirmation():
    user_confirmed = False
    while user_confirmed == False:
        random_restaurant = random_item_picker(restaurants_list)
        user_input = input(f'Would you like to keep {random_restaurant} as your selected restaurant? y/n ')
        if user_input == 'y':
            print(f'Thanks for choosing {random_restaurant}')
            return random_restaurant
        else:
            print('another option will be generated for you!')


def controller():
    destination_selection = user_restaurant_confirmation()
    restaurant_selection = user_restaurant_confirmation()
    print(f'Thank you for choosing {destination_selection} and {restaurant_selection}')  

controller()