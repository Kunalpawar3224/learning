array = [2, 6, 7, 4, 13, 11]
n = len(array)

for i in range(n-1):
    for j in range(n-i-1):
        if array[j+1] < array[j]:
            array[j], array[j+1] = array[j+1], array[j]

print("Sorted Array = ", array)