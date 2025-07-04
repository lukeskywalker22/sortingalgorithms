unsorted_list = [1, 56, 6, 76, 34, 40, 95, 111, 32, 67]

def bubble_sort_forloop(numlist):
    for i in range(len(numlist) - 1):
        for j in range(len(numlist) - 1):
            if numlist[j] > numlist[j+1-i]:
                temp = numlist[j]
                numlist[j] = numlist[j+1]
                numlist[j+1] = temp
    
    print('iterations:', i)
    return numlist

def bubble_sort_whileloop(numlist):
    i = 0
    j = 0
    isSwapped = True
    while i < len(numlist) and isSwapped:
        isSwapped = False
        while j < len(numlist) - 1 - i:
            if numlist[j] > numlist[j+1]:
                isSwapped = True
                temp = numlist[j]
                numlist[j] = numlist[j+1]
                numlist[j+1] = temp
            j += 1
        i += 1
    
    print('iterations:', i)

    return numlist
    

print(bubble_sort_forloop(unsorted_list))
print(bubble_sort_whileloop(unsorted_list))