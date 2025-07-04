unsorted_list = [1, 56, 6, 76, 34, 40, 95, 111, 32, 67, 67]

def quick_sort(numlist):
    if len(numlist) < 2:
        return numlist
    pivot = numlist[-1]
    smallerElements = []
    largerElements = []
    del numlist[-1]
    for element in numlist:
        if element < pivot:
            smallerElements.append(element)
        elif element > pivot:
            largerElements.append(element)
    
    return quick_sort(smallerElements) + [pivot] + quick_sort(largerElements)

def quick_sort_optimised(numlist):
    if len(numlist) < 2:
        return numlist
    pivot = numlist[-1]
    smallerElements = []
    largerElements = []
    del numlist[-1]
    for element in numlist:
        if element < pivot:
            smallerElements.append(element)
        elif element > pivot:
            largerElements.append(element)
    
    return quick_sort(smallerElements) + [pivot] + quick_sort(largerElements)

    
print(quick_sort(unsorted_list))
