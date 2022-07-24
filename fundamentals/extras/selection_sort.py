

test_array = [5, 6, 9, 4, 0, 1, 1, 22, 17, 2, 1, 5]

def selection_sort(array):
    
    for i in range(0,len(array)-1):
        temp = array[i]
        k = i
        for j in range(i+1,len(array)):
            if array[j] < temp:
                k = j
                temp = array[k]
        array[k] = array[i]
        array[i] = temp

    return array

print(selection_sort(test_array))