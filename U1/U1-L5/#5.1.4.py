# 5.1.4 想出 5 个旅游的目的地
# 将心愿单存储在列表 travel_list 中，并确保这些地点不是按字母顺序排列的
travel_list = ["London", "North pool", "Venice", "Everest", "Camp Nou"]
# 按原始排列顺序打印心愿单，不要考虑输出是否整洁的问题，只管打印原始列表
print(travel_list)
# 按字母顺序打印心愿单的每个地点，但不要修改 travel_list，再次打印心愿单，核实排列顺序未变
a = travel_list.copy
print(a)
print(travel_list)
# 按与字母顺序相反的顺序打印每个地点，但不要修改 travel_list，再次打印心愿单，核实排列顺序未变
a = travel_list.copy()
a.sort(reverse=True)
print(a)
print(travel_list)
# 将心愿单逆序排列，打印心愿单，核实排列顺序确实变了
travel_list.reverse()
print(travel_list)
# 再次将心愿单逆序排列，打印心愿单，核实已恢复到原来的排列顺序
travel_list.reverse()
print(travel_list)
# 修改心愿单，使地点按字母顺序排列。打印心愿单，核实排列顺序确实变了
travel_list.sort()
print(travel_list)
# 再次修改心愿单，使地点按与字母顺序相反的顺序排列。打印心愿单，核实排列顺序确实变了
travel_list.sort(reverse=True)
print(travel_list)




