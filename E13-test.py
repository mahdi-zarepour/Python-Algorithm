# [3, 8, 1, 6, 54, 12] => [1, 3, 6, 8, 12, 54]

def bead_sort(array):
    if any(not isinstance(i, int) or i < 0 for i in array):
        raise TypeError('squence must be list of non-negative integers.')

    for _ in range(len(array)):
        for i, (rod_upper, rod_lower) in enumerate(zip(array, array[1:])):
            if rod_upper > rod_lower:
                array[i], array[i + 1] = array[i + 1], array[i]
    return array


print(bead_sort([3, 8, 1, 6, 6, 54, 12]))



