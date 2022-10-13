def move_items(x, direction="right", list_input=[]):
    if direction == "left":
        for j in range(0, x):
            list_input.append(list_input[0])
            list_input.pop(0)
    elif direction == "right":
        for j in range(0, x):
            a = len(list_input)-1
            list_input.insert(0, list_input[a])
            list_input.pop()
    return list_input


print(move_items(1, "right", [1, 2, 3, 4]))


