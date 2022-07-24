

test_array1 = [5, 6, 9, 4, 0, 1, 1, 22, 17, 2, 1, 5]
test_array2 = [7]
test_array3 = [9, 5, 5, 5, 5, 5, 5]

def selection_sort(array):
    if len(array) == 1:
        return array

    for i in range(0,len(array)-1):
        temp = array[i]
        k = i
        for j in range(i+1,len(array)):
            if array[j] < array[k]:
                k = j
        array[k], array[i] = array[i], array[k]
    return array

print(selection_sort(test_array1))
print(selection_sort(test_array2))
print(selection_sort(test_array3))