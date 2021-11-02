"""

    Last Occurrence
        [1, 2, 2, 2, 3, 4, 4, 5], 4 => 6

"""



def last_occurrence(array, target):
    low, high = 0, len(array)-1

    while low <= high:
        mid = (low + high) // 2

        if (array[mid] == target and mid == len(array)-1) or \
            (array[mid] == target and array[mid + 1] > target):
            return mid
        elif (array[mid] <= target):
            low = mid + 1
        else:
            high = mid - 1
        


print(last_occurrence([1, 2, 2, 2, 3, 4, 4, 5], 4))