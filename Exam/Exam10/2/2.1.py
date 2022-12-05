def max_profit(prices: list[int]) -> int:
    min = prices[0]
    profit = 0
    for i in range(len(prices)):
        if min > prices[i]:
            min = prices[i]
        if profit < prices[i] - min:
            profit = prices[i] - min
    return profit
# 正确的逻辑


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