''' Script to generate random array of n elements '''

import random

''' Function to generate array of 3000 random integers
Parameters: None
Returns: Array of 3000 random integers'''
def generate_array():
    array = []
    for i in range(3000):
        array.append(random.randint(0, 3000))
    return array