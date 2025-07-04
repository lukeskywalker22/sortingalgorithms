unsorted_list = [1, 56, 6, 76, 34, 40, 95, 111, 32, 67]

def merge_sort(lst):
    if len(lst) < 2:
        return lst
    
    left = []
    right = []
    sorted_list = []
    
    mid = len(lst) // 2
    left = merge_sort(lst[0:mid])
    right = merge_sort(lst[mid:])

    sorted_list = merge(left, right)
    return sorted_list

def merge(left, right):
    lst = []

    while len(left) != 0 and len(right) != 0:
        if left[0] > right[0]:
            lst.append(right[0])
            del right[0]
        else:
            lst.append(left[0])
            del left[0]
    return lst + left + right
print(merge_sort(unsorted_list))