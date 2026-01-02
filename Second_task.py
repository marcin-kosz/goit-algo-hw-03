import random

def get_numbers_ticket(min_value, max_value, quantity):
    try:
        if min_value < 1:
            print ("Error: min_value must not be smaller than 1")
            return []
        if max_value > 1000:
            print ("Error: max_value must not be greater than 1000")
            return []
        if min_value >= max_value:
            print ("Error: min_value must be smaller than max_value")
            return []
        if quantity > (max_value - min_value + 1):
            print ("Error: quantity must be smaller than max_value")
            return []

        numbers = random.sample(range(min_value, max_value + 1), quantity)
        numbers.sort()
        return numbers
    except TypeError:
        print ("Error: type your number as integer")
