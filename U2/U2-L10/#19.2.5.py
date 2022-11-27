# 19.2.5  Sum of Unique Elements
# You are given an integer array nums.
# The unique elements of an array are the elements that appear exactly once in the array.
# Return the sum of all the unique elements of nums.
def sum_of_unique(nums: list[int]) -> int:
    new_list = []
    for items in nums:
        if nums.count(items) == 1:
            new_list.append(items)
    return sum(new_list)


print(sum_of_unique([1,2,3,2]))
print(sum_of_unique([1,1,1,1,1]))
print(sum_of_unique([1,2,3,4,5]))