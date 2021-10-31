"""

    Linear(Sequential) Search
        [1, 2, 5, 8, 15, 21, 54, 88], 8 => 3

"""

def linear_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return (i, array[i])
        
    return 'Not Found'

print(linear_search([1, 2, 5, 8, 15, 21, 54, 88], 8))