def max_profit(prices: list[int]) -> int:
    profit = []
    if len(prices) == 1:
        profit.append(0)
        return 0
    for x in range(len(prices) - 1):
        for y in range(x + 1, len(prices)):
            profit.append(prices[y] - prices[x])
    if max(profit) > 0:
        return max(profit)
    else:
        return 0
# 垃圾逻辑

fin = open("2.2_test.txt", "r")
a = fin.readlines()
# print(a)
b = []
for i, items in enumerate(a):
    a[i] = items.rstrip("\n")
    b.append(a[i].split(" "))
# print(b)
c = []
for items in b:
    temp = []
    temp.append(items[0])
    temp.append(str(max_profit(list(map(int, list(items[0].split(",")))))))
    c.append(temp)
if c == b:
    print("nice")
# print(max_profit([22,23,14,34,17,41,29,49,37,15,19,44,39,3,21,14,6,17,41,10,11,16,14]))