

test_list1 = [5, 6, 9, 4, 0, 1, 1, 22, 17, 2, 1, 5]
test_list2 = [7]
test_list3 = [9, 5, 5, 5, 5, 5, 5]

def insertion_sort(list):
    if len(list) == 1:
        return list

    for i in range(1,len(list)):
        temp = list[i]
        for j in range(i-1,-1,-1):
            if list[j] <= temp:
                break
            else:
                list[j], list[j+1] = list[j+1], list[j]
    return list


print(insertion_sort(test_list1))
print(insertion_sort(test_list2))
print(insertion_sort(test_list3))