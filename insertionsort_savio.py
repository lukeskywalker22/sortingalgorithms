unsorted_list = [1, 56, 6, 76, 34, 40, 95, 111, 32, 67]

def insertion_sort(unsorted_list):
    lst = unsorted_list
    for i in range(2, len(lst)):
        target = lst[i]
        j = i - 1
        while j > 0 and lst[j] > target:
            lst[j + 1] = lst[j]
            j = j - 1
        lst[j + 1] = target
    return lst
print(insertion_sort(unsorted_list))