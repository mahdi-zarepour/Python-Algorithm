"""

    search range
        [1, 2, 3, 3, 3 ,4, 4, 6], 3 => [2, 4]
        [1, 2, 3, 3, 3 ,4, 4, 6], 10 => [None, None]

    این الگوریتم نوشته شده در این حالت بالا ارور میده

"""


def search_range(array, target):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = low + (high - low) // 2 # جلوگیری از خطای منطقی هنگام کم و زیاد کردن های و لوو
        if target < array[mid]:
            high = mid - 1
        elif target > array[mid]:
            low = mid + 1
        else:
            break

    for i in range(len(array) - 1, -1, -1):
        if array[i] == target:
            return [mid, i]

    return [None, None]



print(search_range([1, 2, 3, 3, 3 ,4, 4, 6], 3))