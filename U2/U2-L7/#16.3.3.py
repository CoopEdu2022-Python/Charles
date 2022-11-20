def find_duplicate_items(nums: list[int]) -> int:
    nums.sort()
    items_count = nums.count(nums[0])
    for i in range(len(nums)):
        if items_count <= nums.count(nums[i]):
            items = nums[i]
            items_count = nums.count(nums[i])
    return items


print(find_duplicate_items([5,1,5,2,5,3,5,4]))
