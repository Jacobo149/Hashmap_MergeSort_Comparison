''' Script to generate random array of n elements '''

import random

''' Function to generate array of 1000 random integers
Parameters: None
Returns: Array of 1000 random integers'''
def generate_array():
    array = []
    for i in range(1000):
        array.append(random.randint(0, 1000))
    return array