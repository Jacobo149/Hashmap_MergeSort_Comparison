''' Program to compare speeds between merge sort and a prime number hashmap
Will test by sending two arrays to check if they are equal to one another '''

import hashmap
import mergesort
import array_generator
#import verifier
import timeit

''' Main function to run program
Parameters: None
Returns: None'''
def main():

    arr1 = array_generator.generate_array() # Creating random array
    arr2 = arr1[:] #Creating shallow copy

    # Time and run hashmap
    h1_start = timeit.default_timer()
    hash_verify, hashmap_time = run_Hashmap(arr1, arr2)
    h1_stop = timeit.default_timer()

    # Time and run mergesort
    m1_start = timeit.default_timer()
    merge_verify, merge_time = run_Mergesort(arr1, arr2)
    m1_stop = timeit.default_timer()

    # Verify arrays are equal and print results
    if (hash_verify == True) and (merge_verify == True):

        print("Verify Time")
        print("Hashmap time: ", hashmap_time)
        print("Mergesort time: ", merge_time)
        print("")
        print("Overhead and Verify Time")
        print("Hashmap time: ", h1_stop - h1_start)
        print("Mergesort time: ", m1_stop - m1_start)
  
    else:
        print("Error: Arrays are not equal")



''' Function to run hashmap on two arrays
Parameters: Two arrays of integers
Returns: Boolean, Time'''
def run_Hashmap(arr1, arr2):
    primes = hashmap.primeNumberGenerator()
    primemap1 = hashmap.mapPrimeNumbers(arr1, primes)
    primemap2 = hashmap.mapPrimeNumbers(arr2, primes)
    h2_start = timeit.default_timer()
    product1 = hashmap.multiplyDictionary(primemap1)
    product2 = hashmap.multiplyDictionary(primemap2)
    h2_stop = timeit.default_timer()

    if product1 == product2:
        return True, h2_stop - h2_start


''' Function to run mergesort on two arrays
Parameters: Two arrays of integers
Returns: Boolean, Time'''
def run_Mergesort(arr1, arr2):
    mergesort.mergeSort(arr1)
    mergesort.mergeSort(arr2)

    m2_start = timeit.default_timer()
    verify = mergesort.equal(arr1, arr2)
    m2_stop = timeit.default_timer()

    return verify, m2_stop - m2_start

if __name__ == "__main__":
    main()