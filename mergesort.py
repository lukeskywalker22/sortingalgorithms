unsorted_list = [1, 56, 6, 76, 34, 40, 95, 111, 32]

def merge(left_array, right_array):
    sortingindex = 0
    sorted_array = []

    while len(right_array) != 0 and len(left_array) != 0:
        if left_array[0] > right_array[0]:
            sorted_array.append(right_array[0])
            del right_array[0]
        else:
            sorted_array.append(left_array[0])
            del left_array[0]

        sortingindex += 1
        print(sorted_array)

    sorted_array += left_array
    sorted_array += right_array

    return sorted_array

def merge_sort(numlist):
    if len(numlist) < 2:
        return numlist
    midindex = len(numlist) // 2
    first_half_array = merge_sort(numlist[0:midindex])
    second_half_array = merge_sort(numlist[midindex:])
    merged_array = merge(first_half_array, second_half_array)

    return merged_array

print(merge_sort(unsorted_list))