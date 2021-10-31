"""

    move zeros
        [True, 10, 'Mahdi', 23, 0, False, 0, 'Ali'] => [True, 10, 'Mahdi', 23, False, 'Ali', 0, 0]

"""

def move_zeros(sequence):
    result = []
    zeros = 0

    for i in sequence:
        if i == 0 and type(i) != bool:
        # if i == 0 and not isinstance(i, bool):
            zeros += 1
        else:
            result.append(i)

    result.extend([0] * zeros)
    return result


print(move_zeros([True, 10, 'Mahdi', 23, 0, False, 0, 'Ali']))