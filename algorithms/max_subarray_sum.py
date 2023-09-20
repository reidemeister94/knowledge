def kadanes_algorithm(array):
    max_sum = -float("inf")
    max_sum_final = -float("inf")
    for elem in array:
        max_sum = max(elem, max_sum + elem)
        max_sum_final = max(max_sum_final, max_sum)
    return max_sum_final
