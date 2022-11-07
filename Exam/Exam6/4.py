def max_sec_average(nums: list, k: int) -> float:
    all_sum = list()
    for i in range(len(nums)):
        all_sum.append(sum(nums[i: i + k]))
        if i + k == len(nums) - 1:
            break
    return (max(all_sum)) / k


print(max_sec_average([1,12,-5,-6,50,3], 4))


