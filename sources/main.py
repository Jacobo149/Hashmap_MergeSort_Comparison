''' Program to compare speeds between merge sort and a prime number hashmap
Will test by sending two arrays to check if they are equal to one another '''

from sources.mergesort import mergeSort
from sources.verifier import verify
from sources.hashmap import hashmap
from sources.array_generator import generate_array

def main():
    # Generate array of 1000 random integers
    arr = generate_array()

    # Generate array of 1000 prime numbers
    primes = primeNumberGenerator()


    # Sort array of 1000 random integers
    arr = mergeSort(arr)