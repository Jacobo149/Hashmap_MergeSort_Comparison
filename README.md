# Hashmap_MergeSort_Comparison
Compares the speed difference between hashmap and merge-sort as to whether two arrays are equal.  
Hashmap maps every element to an prime number and adds the entries to a dictionary. Prime numbers are multipled to see if arrays are equal.  
Merge-sort runs as expected. For loop is used to check that every element in the arrays are equal.

## How to Run

###Prerequisites
- Have Python installed.  
- Download repository to local computer.

### Running the Script
- Navigate to sources directory
- Run main
```
python ./main.py
```

## Results
Run with 13th Gen Intel I7  
Run on arrays of 3000 elements    
Verify Time  
Hashmap time:  0.004408500011777505  
Mergesort time:  0.01814100000774488  

Overhead and Verify Time  
Hashmap time:  10.641749600006733  
Mergesort time:  0.026110599981620908  

###Interpretation of Results
Overhead accounts for the computations needed to get the arrays into a state where they can be verified.  
For the hashmap, this is generating the prime numbers and mapping them to the dictionary.  
For the mergesort, this is the process of sorting the two arrays.

Verify is the time it takes the arrays to be verified as correct, the verify process for both algorithms is dicussed in the beginning of this document.  

###Conclusion
Genrating prime numbers is a computationally-intensive process that eats up a lot of CPU time thus why Overhead and Verify time takes over 10 seconds to complete. Once this overhead is complete, the process of verifying the arrays is a magnitude lower than mergesort. On larger arrays, the difference in speed between the two would be amplified.  
In terms of implementation, if the upper bound of input arrays is known, the prime numbers can be generated beforehand, thus eliminating most computational work required by the algorithm. Mapping the elements and multiplying them for verification is all that would be required. Note that simplification of overhead cannot be done for merge sort. As the merge sort algorithm itself is the overhead.
