#1. 判断是否为 3 的幂
# 定义一个函数 is_power_of_3_v1(n)，参数为整数，判断 n 是否为 3 的幂
def is_power_of_3_v1(n: int) -> bool:
    remainder = 0
    while n > 1:
        remainder = n % 3
        n /= 3
    if remainder == 0 and n == 1:
        return True
    else:
        return False


print(is_power_of_3_v1(-1))


# 定义另一个函数 is_power_of_3_v2(n)，用另一种方式，判断 n 是否为 3 的幂
def is_power_of_3_v2(n: int) -> bool:
    i = 1
    while i < n:
        i *= 3
    if i == n:
        return True
    else:
        return False


print(is_power_of_3_v2(9))
# n 的取值范围为 -2^31 <= n <= 2^31 - 1

