def sum_mult(my_list):
    if not my_list:
        return 0
    sum_even = sum(my_list[i] for i in range(0, len(my_list), 2))
    return sum_even * my_list[-1]
print(sum_mult([0, 1, 7, 2, 4, 8]))
print(sum_mult([1, 3, 5]))
print(sum_mult([6]))
print(sum_mult([]))