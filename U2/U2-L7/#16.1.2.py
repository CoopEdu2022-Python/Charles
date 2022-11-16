def matrix_diagonal_sum(matrix: list[list[int]]) -> int:
    result = 0
    reverse_matrix = []
    for i, list in enumerate(matrix):
        result += list[i]
        reverse_matrix.append(sorted(list, reverse=True))
    for i, list in enumerate(reverse_matrix):
        if 2 * i + 1 == len(reverse_matrix):
            continue
        result += list[i]
    return result


print(matrix_diagonal_sum([[5]]))
