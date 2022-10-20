verdict_list = []


def is_haha_number(number):
    number = str(number)
    new = 0
    for item in number:
        new += pow(int(item), 2)
    verdict_list.append(new)
    if 1 in verdict_list:
        return True
    if sorted(list(set(verdict_list))) != sorted(verdict_list):
        return False
    return is_haha_number(new)


print(is_haha_number(24))
