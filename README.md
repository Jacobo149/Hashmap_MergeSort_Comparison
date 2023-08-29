# Hashmap_MergeSort_Comparison
Compares the speed difference between hashmap and merge-sort as to whether two arrays are equal.  
Hashmap maps every element to a prime number and adds the entries to a dictionary. Prime numbers are multiplied to see if arrays are equal.  
Merge-sort runs as expected. For loop is used to check that every element in the arrays is equal.

## How to Run

### Prerequisites
- Have Python installed.  
- Download the repository to local machine.

### Running the Script
- Navigate to the sources directory
- Run main
```
python ./main.py
```

## Results
Run with 13th Gen Intel I7  
Run on arrays of 3000 elements    
<br />
Verify Time  
Hashmap time:  0.004408500011777505  
Mergesort time:  0.01814100000774488  

Overhead and Verify Time  
Hashmap time:  10.641749600006733  
Mergesort time:  0.026110599981620908  

### Interpreting of Results
Overhead accounts for the computations needed to get the arrays into a state where they can be verified.  
The hashmap generates the prime numbers and maps them to the dictionary.  
For merge sort, this is the process of sorting the two arrays.

Verify is the time it takes the arrays to be verified as correct, the verification process for both algorithms is discussed at the beginning of this document.  

### Conclusion
Generating prime numbers is a computationally-intensive process that eats up a lot of CPU time thus why Overhead and Verify time takes over 10 seconds to complete. Once this overhead is complete, verifying the arrays is a magnitude lower than mergesort. On larger arrays, the difference in speed between the two would be amplified.  
In terms of implementation, if the upper bound of input arrays is known, the prime numbers can be generated beforehand, thus eliminating most computational work required by the algorithm. Mapping the elements and multiplying them for verification is all that would be required. Note that simplification of overhead cannot be done for merge sort. As the merge sort algorithm itself is the overhead.
