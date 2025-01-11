# src = https://www.w3schools.com/dsa/dsa_algo_insertionsort.php


array = [64, 34, 25, 5, 22, 11, 90, 12]

n = len(array)
#Applied simple logic here
# The algorithm takes one value at a time from the unsorted part of the array and puts it into the 
# right place in the sorted part of the array, until the array is sorted.
for i in range(1, n):
    # iterate from 0 to the ith element to sort the arrar till ith element 
    for j in range(0,i):
        if array[j] > array[i]:
            array[j], array[i] = array[i], array[j]

print(array)