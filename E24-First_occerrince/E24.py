"""

    First Occerrence
        [1, 2, 2, 2, 3, 4, 4, 5], 4 => 5

"""


def first_occerrence(array, target):
    low, high = 0, len(array)-1

    while low <= high:
        mid = (low + high) // 2
        if low == high:
            break
        if array[mid] < target:
            low = mid + 1
        else:
            high = mid
    
    if array[low] == target:
        return low


print(first_occerrence([1, 2, 2, 2, 3, 4, 4, 5], 4))


        