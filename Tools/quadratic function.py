def roots_for_quadratic_function(a, b, c):
    return (-b + ((b ** 2 - (4 * a * c)) ** 0.5)) / (2 * a), (-b - ((b ** 2 - (4 * a * c)) ** 0.5)) / (2 * a)

print(roots_for_quadratic_function(-0.5 * 9.8, 1, 600))
