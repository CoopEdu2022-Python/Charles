# 5.1.1 为以下列表尝试以上 14 种方法，每一步操作后，打印当前的列表
num_list = [1, 2, 3, 4, 5]
num_list.insert(0, 0)
print('step 0 :', num_list)
num_list.append(6)
print("step 1: ", num_list)
num2_list = [7, 8, 9]
num_list.extend(num2_list)
print("step 2: ", num_list)
num_list.remove(0)
print("step 3: ", num_list)
num_list.pop()
print("step 4: ", num_list)
num_list.clear()
print("step 5: ", num_list)
num_list = [1, 4, 2, 3, 5]
num_list[0] = 0
print("step 6: ", num_list)
num_list.sort()
print("step 7: ", num_list)
num_list.sort(reverse=True)
print("step 8: ", num_list)
num_list.reverse()
print("step 9: ", num_list)
print("step 10: ", len(num_list))
print("step 11: ", num_list.count(3))
del num_list[2]
print("step 12: ", num_list)
del num_list
print("step 13: ", num_list)




