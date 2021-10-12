"""

    Top One
        [1, 1, 2, 2, 3] => [1, 2]

"""

"""
در الگوریتمی که در سند اپیزود8 نوشتم داشتم از متود مکس که یکی از متود های داخلی
پایتون است برای بدست آوردن بزرگ ترین ولیو از دیکشنری ولیوز استفاده میکردم.
از اونجایی که ما در الگوریتم نویسی بدنبال افزایش قدرت حل مسئله هستیم، من از متود
بابل سورت استفاده کردم تا از حداقل امکانات بیشترین بهره رو ببریم.

"""



# O(n^2)
def bubble_sort(array):
    length = len(array)

    for i in range(length):
        swapped = False
        for j in range(length - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if not swapped:
            break

    return array



# O(n)
def top(array):
    values = {}
    f_value = 0

    for i in array:
        if i in values:
            values[i] += 1
        else:
            values[i] = 1
        
    list_values_value = [i for i in values.values()]
    f_value = bubble_sort(list_values_value)[-1]

    for i in values.keys():
        if values[i] == f_value:
            result = [i]
        else:
            continue

    return result, f_value



print(top([1, 1, 2, 2, 3, 3, 3, 3, 3]))




    
