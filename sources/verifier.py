''' Will check if the two arrays are equal to one another
Not necessary for my purposes,
but if someone wants to use this for their own purposes, they can verify the arrays are equal '''

import numpy as np

''' Function to check if two arrays are equal
Parameters: Two arrays of integers
Returns: Boolean '''
def verify(arr1,arr2):
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)

    return arr1 == arr2