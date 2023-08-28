# Functions to create prime numbers, map them to the given array,
# and multiply them to find the product

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

def mapPrimeNumbers(arr, primes):
    primeMap = {}
    for i in range(len(arr)):
        primeMap[primes[i]] = arr[i]
    return primeMap

def multiplyDictionary(primeMap):
    product = 1
    for key in primeMap:
        product *= key
    return product

