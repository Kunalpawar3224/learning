# QuickSort function
def quicksort(arr):
    # Base case: if the array has 0 or 1 element, it's already sorted
    if len(arr) <= 1:
        return arr
    else:
        # Choose the pivot (usually the last element)
        pivot = arr[-1]
        
        # Partition the array into three parts:
        # Elements less than pivot, equal to pivot, and greater than pivot
        less_than_pivot = [x for x in arr[:-1] if x <= pivot]
        
        greater_than_pivot = [x for x in arr[:-1] if x > pivot]
        
        print( "less_than_pivot = ", quicksort(less_than_pivot))
        # Recursively apply quicksort on both subarrays
        return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)

# Example usage
arr = [7, 2, 1, 6, 8, 5, 3, 4]
sorted_arr = quicksort(arr)
print("Sorted Array:", sorted_arr)
