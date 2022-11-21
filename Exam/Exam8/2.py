def array_sign(nums: list[int]) -> int:
    negative = 0
    for i in nums:
        if i < 0:
            negative += 1
        elif i == 0:
            return 0
    if negative % 2 == 0:
        return 1
    else:
        return -1


print(array_sign([-1,1,-1,1,-1]))
