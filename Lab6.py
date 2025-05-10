def power_bruteforce(a, n):
    result = 1
    for _ in range(n):
        result *= a
    return result

def power(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return power(a * a, n // 2)
    else:
        return a * power(a * a, n // 2)

a, n = map(int, input("Enter the value of a and n: ").split())
result_brute = power_bruteforce(a, n)
result_divide_conquer = power(a, n)
print("Result using brute force:", result_brute)
print("Result using divide and conquer:", result_divide_conquer)
