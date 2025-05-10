def factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact

def binomialCoeff(n, k, method='brute'):
    if method == 'brute':
        return factorial(n) // (factorial(k) * factorial(n - k))
    else:
        C = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            for j in range(min(i, k) + 1):
                C[i][j] = 1 if j == 0 or j == i else C[i - 1][j - 1] + C[i - 1][j]
        return C[n][k]

n = int(input("Enter the value of n: "))
k = int(input("Enter the value of k: "))

result_bruteForce = binomialCoeff(n, k, method='brute')
result_DP = binomialCoeff(n, k, method='dp')

print(f"Binomial Coefficient (Brute Force): {result_bruteForce}")
print(f"Binomial Coefficient (Dynamic Programming): {result_DP}")
