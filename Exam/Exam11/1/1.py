def longest_common_prefix(strs: list[str]) -> str:
    strs = sorted(strs, reverse=True)
    temp_old = []
    i = 1
    while 1:
        temp_new = []
        for items in strs:
            temp_new.append(items[:i])
        if len(set(temp_new)) != 1:
            print(temp_old[0])
            return temp_old[0]
        temp_old = temp_new
        i += 1


# with open("1.txt", "r") as f:
#     overall_list = f.readlines()
#     check_list = []
#     for items in overall_list:
#         a, b = items.split(" ")[0], items.split(" ")[1].strip("\n")
#         a = a.split(",")
#         c = longest_common_prefix(a)
#         if c == b:
#             check_list.append(1)
# print(check_list)
# if len(set(check_list)) == 1:
#     print("Nice")
a = "qmtou,qmmf,qmpcf,qmwt,qmmkso,qmecsp,qmtp,qmz,qmarmvd,qmu".split(",")
print(sorted(a))
# print(longest_common_prefix(a))