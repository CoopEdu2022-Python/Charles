def fill_cups(amount: list[int]) -> int:
    count = 0
    amount.sort(reverse=True)
    while 1:
        amount[0] -= 1
        amount[1] -= 1
        amount.sort(reverse=True)
        if amount[1] == 0:
            count += amount[0] + 1
            break
        count += 1
    return count


print(fill_cups([1,4,2]))
print(fill_cups([5,4,4]))
print(fill_cups([5,0,0]))
