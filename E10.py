"""

    is isomorphic
        foo, bae => False
        foo, bee => True



    این الگوریتم دو استرینگ را گرفته و مشخص میکند که آیا این دو رشته با یکدیگر متقارن هستند یا نه.
    روش کار این الگوریتم به این شکل است که ابتدا تعداد کاراکترهای دو استرینگ را با هم مقایسه میکند
    و اگر با یکدیگر برابر نبودند False برگشت داده میشود
    در صورت برابر بودن تعداد کاراکترها، حروف هر استرینگ را با حروف استرینگ دیگر متناظر قرار میدهد
    و در صورت تکرار حروف، باید با حرفی که قبلا متناظر بوده برابر باشد. در غیر اینصورت فالس برگشت داده خواهد شد

"""



def is_isomorphic(str_1, str_2):
    if len(str_1) != len(str_2):
        return False

    dic = {}
    set_value = set()

    for i in range(len(str_1)):
        if str_1[i] not in dic:
            if str_2[i] in set_value: return False
            dic[str_1[i]] = str_2[i]
            set_value.add(str_2[i])
        else: 
            if dic[str_1[i]] != str_2[i]: return False

    return True

print(is_isomorphic(str_1='ali', str_2='ktt'))




