## File to generate random array of 10000 elements ###

import random

def generate_array():
    array = []
    for i in range(10000):
        array.append(random.randint(0, 1000))
    return array


if __name__ == "__main__":
    print(generate_array())