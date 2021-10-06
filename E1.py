"""

    Complexity 
    Time  Space

"""

numbers = [1, 2, 5, 7, 98, 23, 65, 47, 89, 44, 55, 88, 47, 578, 69]

def show(list, element):
    for i in list:
        if i == element:
            return list.index(i)

print(show(numbers, 578))


"""

    این الگوریتم در اینپوت های بزرگ میخواد دونه دونه بگرده
    پس اگر یک میلیون عضو داشته و آخرینش باشه اون چیزی
    که مد نظر ما هست، کلی طول میکشه تا پیدا بشه

"""
