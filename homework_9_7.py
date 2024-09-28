def is_prime(func):
    def simple_hard(*args, **kwargs):
        result = func(*args, **kwargs)
        b = 0
        for y in range(1, result+1):
            if result % y == 0:
                b += 1
        if b > 2:
            print('Составное')
        else:
            print('Простое')
        return result
    return simple_hard



@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)