"""

    bead sort
        [3, 8, 1, 6, 54, 12] => [1, 3, 6, 8, 12, 54]
    non-negative or x < 0

"""

def bead_sort(squence):
    """
    فانکشن انی از ما یک ایتریبل میگیره و یک سری شروطی رو چک میکنه و اگر یکی از شرط ها ترو بود میره شرط اصلی اجرا میشه
    فانکشن اینستنس برای ما چک میکنه که مقداری که بهش دادیم از چه نوع تایپیی است
    """
    if any(not isinstance(x, int) or x < 0 for x in squence):
        raise TypeError('squence must be list of non-negative integers.')


    """
    برای ما در حلقه اول مهمه که به تعداد لن سیکواس بچرخیم و زمانی که مقداری که قراره برگرده مهم نیست از آندرلاین استفاده میکنیم

    """
    for _ in range(len(squence)):
        for i, (rod_upper, rod_lower) in enumerate(zip(squence, squence[:1])):
            if rod_upper > rod_lower:
                squence[i] -= rod_upper - rod_lower
                squence[i + 1] += rod_upper - rod_lower

    return squence


print(bead_sort([1, 74, 98, 54, 12]))