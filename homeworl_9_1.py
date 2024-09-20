def apply_all_func(int_list, *functions):
    result = {}
    for func in functions:
        i = func(int_list)
        result[func.__name__] = i
    return result

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))