unsorted_list = [1, 56, 6, 76, 34, 40, 95, 111, 32, 67, 3456, 234, 345 , 23 , 55]

def bubble_sort(lst):
    sorted_list = lst
    iterations = 0
    for i in range(len(sorted_list)):
        iterations = i
        for j in range(len(sorted_list) - 1):
            if sorted_list[j] > sorted_list[j + 1]:
                temp = sorted_list[j]
                sorted_list[j] = sorted_list[j + 1]
                sorted_list[j + 1] = temp
    print(iterations)
    return sorted_list

def bubble_sort_optimized(lst):
    sorted_list = lst
    i = 0
    swapped = True
    iterations = 0
    while i < (len(sorted_list) - 1) and swapped == True:
        swapped = False
        j = 0
        while j < (len(sorted_list) - 1 - i):
            if sorted_list[j] > sorted_list[j + 1]:
                temp = sorted_list[j]
                sorted_list[j] = sorted_list[j + 1]
                sorted_list[j + 1] = temp
                swapped = True
            j += 1
        i += 1
        iterations += 1
    print(iterations)     
    return sorted_list

print(bubble_sort(unsorted_list))
print(bubble_sort_optimized(unsorted_list))