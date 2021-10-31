# Polynomial Time O(n^n)

numbers = [1, 2, 74, 12, 4, 45, 69, 25, 10]


def bubble_sort(collection):
    length = len(collection)
    for i in range(length - 1):
        swapped = False
        for j in range(length - 1 - i):
            if collection[j] > collection[j + i]:
                swapped = True
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
        if not swapped:
            break
    return collection


print(bubble_sort(numbers))