unsorted_list = [1, 56, 6, 76, 34, 40, 95, 111, 32, 67]

def bubble_sort(lst):
    sorted_list = lst
    for i in range(len(sorted_list)):
        for j in range(len(sorted_list) - 1):
            if sorted_list[j] > sorted_list[j + 1]:
                temp = sorted_list[j]
                sorted_list[j] = sorted_list[j + 1]
                sorted_list[j + 1] = temp
    return sorted_list

print(bubble_sort(unsorted_list))
