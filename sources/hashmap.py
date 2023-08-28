''' Functions to create prime numbers, map them to the given array,
# and multiply them to find the product '''

''' Function to create array of prime numbers
Parameters: None
Returns: Array of Primes '''
def primeNumberGenerator():
    primes = []
    iterator = 2
    
    while len(primes) < 1000:
    
    # Assume number is prime until shown it is not. 
        isPrime = True
        for num in range(2, iterator):
            if iterator % num == 0:
                isPrime = False
      
        if isPrime:
            primes.append(iterator)

        iterator += 1


    return primes

''' Function to map prime numbers to the given array
Parameters: Array of integers, Array of prime numbers
Returns: Hashmap of prime numbers mapped to the given array '''
def mapPrimeNumbers(arr, primes):
    primeMap = {}
    for i in range(len(arr)):
        primeMap[primes[i]] = arr[i]
    return primeMap

''' Function to multiply the prime numbers in the hashmap
Parameters: Hashmap of prime numbers mapped to the given array
Returns: Product of the prime numbers in the hashmap '''
def multiplyDictionary(primeMap):
    product = 1
    for key in primeMap:
        product *= key
    return product

