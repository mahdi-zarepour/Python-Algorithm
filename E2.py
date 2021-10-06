# Constant Time


# big O(1)
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# برای بدست آوردن عضو اول، تعداد آیتم های لیست دیگه اهمیتی نداره. پس بیگ او 1 یا ثابت است


# میخوایم ببینیم عضو اول زوج هست یا نه(ایندکس صفر)
def show(list):
    if list[0] % 2 == 0:
        return 'Even'
    return 'Odd'

print(show(numbers))