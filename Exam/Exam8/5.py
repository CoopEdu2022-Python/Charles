def largest_perimeter(nums: list) -> int:
    nums.sort(reverse=True)
    if (nums[1] + nums[2] > nums[0]) and (nums[0] - nums[2]):
        return sum(nums)
    else:
        return 0


print(largest_perimeter([1, 2, 1]))
print(largest_perimeter([2, 1, 2]))
