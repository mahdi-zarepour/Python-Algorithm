# Linear Time O(n)

numbers = [1, 2, 74, 12, 4, 45, 69, 25, 10]

# Big O(n)
def show(list):
    max_num = list[0]
    for i in list:
        if i > max_num:
            max_num = i
    
    return max_num

print(show(numbers))

