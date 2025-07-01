unsorted_list = [1, 56, 6, 76, 34, 40, 95, 111, 32, 67]

def insertion_sort(numlist):

    for i in range(1,len(numlist)):
        target = numlist[i]
        sortedindex = i - 1
        while sortedindex > 0 and numlist[sortedindex] > target:
            numlist[sortedindex + 1] = numlist[sortedindex]
            sortedindex -= 1
        numlist[sortedindex + 1] = target

    return numlist

print(insertion_sort(unsorted_list))