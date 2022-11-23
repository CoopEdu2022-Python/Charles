def largest_perimeter(nums: list) -> int:
    nums.sort(reverse=True)
    print(nums)
    for i in range(2, len(nums)):
        if nums[1] + nums[i] > nums[0]:
            if nums[0] - nums[i] < nums[1]:
                a = nums[0] + nums[1] + nums[i]
                return a
    else:
        return 0


print(largest_perimeter( [2,1,5,6,9,10,13,7,7,3,2,5,4]))
print(largest_perimeter([2, 1, 2]))
