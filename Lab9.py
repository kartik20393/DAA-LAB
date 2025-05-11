import time
import math

def bruteForce(coef, x):
    return sum(c * math.pow(x, i) for i, c in enumerate(coef))

def horner(coef, x):
    result = 0
    for c in reversed(coef):
        result = result * x + c
    return result

n = int(input("Enter the degree of the polynomial: "))
coef = [float(input("Coefficient for degree {}: ".format(i))) for i in range(n, -1, -1)]
x = float(input("Enter the value of x: "))

start = time.time()
brute_result = bruteForce(coef, x)
print(f"Brute force result: {brute_result:.2f}, time used: {time.time() - start:.6f} seconds")

start = time.time()
horner_result = horner(coef, x)
print(f"Horner’s rule result: {horner_result:.2f}, time used: {time.time() - start:.6f} seconds")
