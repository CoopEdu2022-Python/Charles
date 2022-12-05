def max_profit(prices: list[int]) -> int:
    profit = []
    for x in range(len(prices)-1):
        if len(prices) == 1:
            profit.append(0)
            break
        for y in range(x + 1, len(prices)):
            profit.append(prices[y] - prices[x])
    print(profit)
    return max(profit)


fin = open("2.2_test.txt", "r")
a = fin.readlines()
print(a)
b = []
for i, items in enumerate(a):
    a[i] = items.rstrip("\n")
    b.append(a[i].split(" "))
print(b)
c = []
for items in b:
    temp = []
    temp.append(items[0])
    temp.append(str(max_profit(list(map(int, list(items[0].replace(",", "")))))))
if c == b:
    print("nice")