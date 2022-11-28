def fill_cups(amount: list[int]) -> int:
    count = 0
    while 1:
        amount.sort(reverse=True)
        amount[0] -= 1
        amount[1] -= 1
        for i, items in enumerate(amount):
            if items == 0:
                amount.pop(i)
        if len(amount) == 1:
            count += amount[0] + 1
            break
        count += 1
    return count


print(fill_cups([1,4,2]))
print(fill_cups([5,4,4]))

