# Limit

"""

    [1, 2, 3, 4, 5]
        min 3 => [3, 4, 5]
        max 3 => [1, 2, 3]
        min, max 3 => [3]

"""

"""
در الگوریتم زیر لیستی که دریافت میکنیم مستقیم میره داخل ریترن
بعد با لیست کامپریشن میایم و هر کدوم از اعداد لیست رو 
میریزیم داخل اون دوتا متغییر که نوشتیم 
بعد چک میشه که آیا اون مقدار باتوجه به شرط ترو یا فالس میشه
بعد در اون لیست کامپریشن که نوشتیم اعداد به داخل لیست اضافه میشن یانه

"""

def limit(array, min=None, max=None):
    min_check = lambda val: True if min is None else (val >= min)
    max_check = lambda val: True if max is None else (val <= max)

    return [val for val in array if min_check(val=val) and max_check(val=val)]



numbers = [1, 2, 3, 4, 5]
print(limit(numbers, max=4))




"""
همین الگوریتم رو با استفاده از فانکشن معمولی نوشتم
این روش برای آماتورها و جونیورهاست
بدون نظم هستش و خیلی هم کد باید براش نوشت

"""


def limit_fbv(array, min=None, max=None):
    l = []

    if min:
        for val in array:
            if val >= min:
                l.append(val)

    if max:
        for val in array:
            if val <= max:
                l.append(val)

    print(l)

numbers = [1, 2, 3, 4, 5]
limit_fbv(numbers, max=4)

