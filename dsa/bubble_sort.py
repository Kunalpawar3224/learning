array = [2, 6, 7, 4, 13, 11]
n = len(array)

# make multiple passes over the list until it's fully sorted
for i in range(n-1):
    # Inner loop: This loop iterates over the unsorted part of the list
    # It compares adjacent elements and swaps them if needed
    for j in range(n-i-1):
        # If the current element is greater than the next element, swap them
        if array[j+1] < array[j]:
            array[j], array[j+1] = array[j+1], array[j]

print("Sorted Array = ", array)