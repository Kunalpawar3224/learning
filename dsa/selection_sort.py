# src = https://www.w3schools.com/dsa/dsa_algo_selectionsort.php

my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)
for i in range(n):
    # Assume the first element in the unsorted part is the smallest
    min_index = i
    # inner loop searches for the minimum element in the unsorted part
    for j in range(i+1, n):
        # If a smaller element is found. Update the index of the minimum element
        if my_array[j] < my_array[min_index]:
            min_index = j   
    # Swap the current element (i-th element) with the smallest element found (min_index)
    my_array[i], my_array[min_index] = my_array[min_index], my_array[i]
print("Sorted array:", my_array)