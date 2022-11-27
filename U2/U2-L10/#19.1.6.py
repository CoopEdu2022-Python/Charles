# 定义一个函数 triangle(a, b, c)，判断三个参数是否能构成一个三角形
# 如果不能则抛出异常 IllegalArgumentException，显示异常信息 'a, b, c 不能构成三角形'
# 如果可以构成，打印三角形三个边长
# 在方法中得到命令行输入的三个整数，调用此方法，并捕获异常
class IllegalArgumentException(Exception):
    pass


def triangle(a, b, c) -> int:
    nums = [a, b, c]
    nums.sort(reverse=True)
    if nums[1] + nums[2] > nums[0] and nums[0] - nums[2] < nums[1]:
        return sum(nums)
    raise IllegalArgumentException("a, b, c 不能构成三角形")


a = int(input("请输入a： "))
b = int(input("请输入b： "))
c = int(input("请输入c： "))
try:
    print(triangle(a, b, c))
except Exception as result:
    print("Error: %s" % result)
