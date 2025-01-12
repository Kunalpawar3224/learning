
# First Implemntation
def duplicates1(array):

    n = len(array)
    for i in range(n-1):
        n = len(array)
        for j in range(i+1, n-1):
            if array[i] == array[j]:
                array.pop(j)

    print(array)
    return array



####################

# Second implementation
def duplicates2(array):

    # Remove duplicates by converting to a set
    a = list(set(array))

    print(a)
    return a

array = [1, 7, 34, 12, 7, 23, 34, 9, 11, 1, 3]
# duplicates1(array)
duplicates2(array)