import timeit
import random
import matplotlib.pyplot as plt

def input_array(n):
    return [random.randint(1, 50) for _ in range(n)]

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

trail = int(input("Enter number of trials: "))
N, CPU = [], []

for t in range(trail):
    n = int(input(f"Enter number of elements for trial {t+1}: "))
    arr = input_array(n)
    start = timeit.default_timer()
    selection_sort(arr)
    elapsed_time = (timeit.default_timer() - start) * 1_000_000  
    print(f"Sorted Array: {arr}")
    N.append(n)
    CPU.append(round(elapsed_time, 2))

plt.plot(N, CPU)
plt.scatter(N, CPU, color="red", marker="*", s=50)
plt.xlabel('Array Size – N')
plt.ylabel('CPU Processing Time (μs)')
plt.title('Selection Sort Time Efficiency')
plt.show()
