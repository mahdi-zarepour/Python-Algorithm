"""

    buy-sell stock
        [7, 1, 3, 5, 6, 4] => 5
        [9, 7, 6, 4, 3, 1] => 0

    الگوریتم تمیزی نیست
"""


def max_profit(prices):
    cur_max = 0 # زمانی که داریم داخل حقه میچرخیم، بیشترین مقدار رو میریزه داخل این متغییر
    max_so_far = 0 # در کل حلقه ها، بیشترین مقدار رو نگه میداره

    for i in range(1, len(prices)):
        cur_max = max(0, (cur_max + prices[i] - prices[i - 1]))
        max_so_far = max(max_so_far, cur_max)

    return max_so_far


print(max_profit([7, 3, 1, 5, 6, 5]))