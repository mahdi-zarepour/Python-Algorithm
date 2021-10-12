""""

    Caesar Cipher
        Mahdi, key3 => Pdkgl

"""


"""
    رمزنگاری:
    در این الگوریتم برای رمزنگاری داریم با شیفت کردن نسبت به مقدار عددی که دادیم بهش،
    حروف رو جلو عقب میکنیم و نتیجه رو بر میگردونیم 

    رمزگشایی:
    داریم از همون الگو رمزنگاری استفاده میکنیم ولی با کلید منفی

    بروت_فورس:
    این دفعه با استفاده از متود رمزگشایی میایم و تمام حالت های ممکنه رو بررسی میکنیم
    و در یک دیکشنری قرار میدیم و بعد از اتمام کار، میتونیم عبارت معنادار رو بیابیم

"""

from string import ascii_letters, ascii_lowercase

# Encrypte
def encrypt(string, key):
    alpha = ascii_letters
    result = ''

    for ch in string:
        if ch not in alpha:
            result += ch
        else:
            new_key = (alpha.index(ch) + key) % len(alpha)
            result += alpha[new_key]

    return result

# print(encrypt('Mahdi', 3))



# Decryte
def decrypt(string, key):
    key *= -1
    return encrypt(string, key)

# print(decrypt('Pdkgl', 3))



# Brute Force
def brute_force(string):
    alpha = ascii_letters
    key = 1
    result = ''
    brute_force_data = {}

    while key < len(alpha) + 1:
        result = decrypt(string, key)
        brute_force_data[key] = result
        result = ''
        key += 1

    return brute_force_data

print(brute_force('Pdkgl'))