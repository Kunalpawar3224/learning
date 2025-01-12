array = [1, 7, 34, 12, 7, 23, 34, 9, 11, 1, 3]

n = len(array)
for i in range(n-1):
    n = len(array)
    for j in range(i+1, n-1):
        print("array[i], array[j] = ", array[i], array[j])
        if array[i] == array[j]:
            print("j = ", j)
            array.pop(j)

print(array)

    