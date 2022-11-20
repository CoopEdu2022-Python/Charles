def shuffle_array(nums: list[int]) -> list[int]:
    nums_x = nums[0:int(len(nums)/2)]
    nums_y = nums[int(len(nums)/2):]
    new_list = []
    for i in range(0, int(len(nums)/2)):
        new_list.append(nums_x[i])
        new_list.append(nums_y[i])
    return new_list


print(shuffle_array([2,5,1,3,4,7]))
print("--------------")
print(shuffle_array([1,2,3,4,4,3,2,1]))
print("-----------------")
print(shuffle_array([1,1,2,2]))
