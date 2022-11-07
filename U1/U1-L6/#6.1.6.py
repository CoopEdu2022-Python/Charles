# 6.1.6 定义一个函数，参数为 1 个字符串，将 a-z, A-Z 改为 z-a, Z-A，返回新的字符串
# 例如，参数为 'abcABC'，返回 'zyxZYX'
def change(str_input):
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    for char in str_input:
        if char in lower:
            result += lower[-(lower.find(char) + 1)]
        elif char in upper:
            result += upper[-(lower.find(char) + 1)]
    return result


def invert_alpha(str_input):
    forward = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    backward = "zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA"
    return str_input.translate(str.maketrans(forward, backward))


print(change("abcABC"))
print(invert_alpha("abcABC"))

