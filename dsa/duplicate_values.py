#TODO: Because of remove methon the logic is not working correctly for 1st index
# As the 0th index is also duplicate it is removing that index.
#Fo for 0th index now the 7 no. comes and hence the outer loop is not iterating again on it.
#Hence the 7 no. is duplicating here. 
array = [1, 7, 34, 12, 7, 23, 34, 9, 11, 1, 3]

n = len(array)
for i in range(n-1):
    n = len(array)
    for j in range(i+1, n-1):
        print("array[i], array[j] = ", array[i], array[j])
        if array[i] == array[j]:
            print("j = ", j)
            # remove method removing the next index element which is duplicate
            array.remove(array[j])
            # array.pop(j)

print(array)

    