import timeit
import random
import matplotlib.pyplot as plt

def generate_array(n):
    return [random.randrange(1, 50) for _ in range(n)]

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

trials = int(input("Enter number of trials: "))
N, CPU = [], []

for _ in range(trials):
    n = int(input("Enter number of elements: "))
    arr = generate_array(n)
    start = timeit.default_timer()
    quicksort(arr, 0, n - 1)
    end = timeit.default_timer()
    N.append(n)
    CPU.append(round((end - start) * 1e6, 2))

print("N", N)
print("CPU (microseconds)", CPU)

plt.plot(N, CPU, marker='*', color='red')
plt.scatter(N, CPU, color='red', s=50)
plt.xlabel('Array Size N')
plt.ylabel('CPU Processing Time (microseconds)')
plt.title('QuickSort Time Efficiency')
plt.show()
