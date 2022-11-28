def calculate_tax(brackets: list[list[int]], income: int) -> float:
    tax = 0
    level = [items[0] for items in brackets]
    level.insert(0, 0)
    percent = [items[1] for items in brackets]
    minus_level = []
    for i in range(1, len(level)):
        minus_level.append(level[i] - level[i - 1])
    for i, items in enumerate(minus_level):
        if income - items > 0:
            income -= items
            tax += items * percent[i] * 0.01
        else:
            tax += income * percent[i] * 0.01
            break
    return tax


print(calculate_tax([[3, 50], [7, 10], [12, 25]], 10))
print(calculate_tax([[1, 0], [4, 25], [5, 50]], 2))
print(calculate_tax([[2, 50]], 0))

