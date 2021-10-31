# Exponential Time O(n^n)

from itertools import chain, combinations
import time


def subsets(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


print(list(subsets(['e', 'r', 4, 5, 0, 56, 'cq', 'z', 90])))