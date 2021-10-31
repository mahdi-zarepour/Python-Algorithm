"""

    Binary Search
        [1, 2, 5, 8, 15, 21, 54, 88], 8 => 3

"""


def binary_search(array, target):
    low, high = 0, len(array) - 1

    while low <= high:
        mid = (high + low) // 2
        value = array[mid]
        if value == target:
            return (mid, array[mid])
        elif value < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return None

print(binary_search([1, 2, 5, 8, 15, 21, 54, 88], 54))
