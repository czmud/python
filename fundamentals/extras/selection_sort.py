

test_list1 = [5, 6, 9, 4, 0, 1, 1, 22, 17, 2, 1, 5]
test_list2 = [7]
test_list3 = [9, 5, 5, 5, 5, 5, 5]

def selection_sort(list):
    if len(list) == 1:
        return list

    for i in range(0,len(list)-1):
        temp = list[i]
        k = i
        for j in range(i+1,len(list)):
            if list[j] < list[k]:
                k = j
        list[k], list[i] = list[i], list[k]
    return list

print(selection_sort(test_list1))
print(selection_sort(test_list2))
print(selection_sort(test_list3))