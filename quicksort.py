unsorted_list = [1, 56, 6, 76, 34, 40, 95, 111, 32, 67]

def quicksort(lst):
    if(len(lst) <= 1):
        return lst
    
    pivot = lst[-1]

    lt_array = []
    gte_array = []
    
    for i in range(len(lst) - 1):
        if lst[i] < pivot:
            lt_array.append(lst[i])
        else:
            gte_array.append(lst[i])
    return quicksort(lt_array) + [pivot] + quicksort(gte_array)

print(quicksort(unsorted_list))

