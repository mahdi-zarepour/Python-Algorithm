"""

    remove min
        [5, 3, 1, 6, -3, 12, 0] => -3

"""

def remove_min(array):
    if len(array) == 0:
        return 'your list empty...'

    storage_stack = []
    min = array[-1]
    for _ in range(len(array)):
        val = array.pop()
        if val <= min:
            min = val
        storage_stack.append(val)
        
    for _ in range(len(storage_stack)):
        val = storage_stack.pop()
        if val != min:
            array.append(val)
    
    return array, min


print(remove_min([5, 3, 1, 6, -3, 12, 0, 11, 0]))