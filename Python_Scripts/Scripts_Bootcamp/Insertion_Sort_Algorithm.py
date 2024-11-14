def insertion_sort(my_list, reverse=False):
    for i in range(1, len(my_list)):
        value = my_list[i]
        j = i
        while j > 0 and my_list[j - 1] > value:
            my_list[j] = my_list[j - 1]
            j -= 1
        my_list[j] = value

    if reverse:
        my_list.reverse()

    return my_list


# Testing the function
print(insertion_sort([3, 1, 4, 1, 5]))
print(insertion_sort([10, 2, 8, 6, 7], reverse=True))