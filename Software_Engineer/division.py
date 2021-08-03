def division(a, b):
    if a == b:
        return 1
    if a < b:
        return 0

    quotient = 1
    temp_number = b

    while temp_number + b <= a:
        quotient += 1
        temp_number += b

    return quotient


print(division(1200, 3))
