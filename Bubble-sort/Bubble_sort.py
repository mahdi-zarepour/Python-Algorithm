# Bubble Sort: O(n^2) and good for Ram(inplace)

# میخوایم بیایم و ایندکس صفر رو با تمام ایندکس ها مقایسه کنیم 
# اگر ایندکس بعدی کوچک تر بود، یدونه میاد عقب
# اگر نه که همین طور ادامه میده تا آخر تا اون هایی که کوچک تر هستند هی یکی برن عقب
# در انتهای مقایسه ایندکس، بزرگ ترین عدد به جایگاه آخر میره و
# در نهایت ایندکس کوچک تر به اول میره و ایندکس بزرگ تر به آخر میره


# لیست مدنظر ما
numbers = [6, 5, 14, 15, 98, 45, 12, 54, 2, 1, 8]


def bubble_sort(collection):
    length = len(collection) 
    for i in range(length): # نیاز داریم تا به تعداد آیتم های موجود در لیست اینکار تکرار بشه
        swapped = False
        for j in range(length - 1 - i):
            if collection[j] > collection[j + 1]:
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
                swapped = True
        if not swapped:
            break

    return collection

print(numbers)
print('-----------')
print(bubble_sort(numbers))