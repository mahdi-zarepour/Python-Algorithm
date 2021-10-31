"""

    Two Sum
        sort numbers: [2, 7, 12, 16], 9 => [1, 2]

"""

def two_sum(numbers, target):
    p1 = 0
    p2 = len(numbers) - 1

    while p1 < p2:
        s = numbers[p1] + numbers[p2]
        if s == target:
            return [p1 + 1, p2 + 1]
        elif s > target:
            p2 -= 1
        else:
            p1 += 1
        
print(two_sum([2, 7, 12, 16], 9))
        