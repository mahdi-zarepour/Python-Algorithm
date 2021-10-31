"""

    rorate
        rotate('hello', 2) => return 'llohe'
        rotate('hello', 5) => return 'hello'
        rotate('hello', 6) => return 'elloh'
        rotate('hello', 7) => return 'llohe'

"""


def rotate(string, angel):
    dubble = string + string
    if angel <= len(string): return dubble[angel:angel + len(string)]
    else: return dubble[angel - len(string):angel]

print(rotate('hello', 7))