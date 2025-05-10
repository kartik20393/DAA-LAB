import time
import matplotlib.pyplot as plt

def linear_search(arr, key):
    for i, v in enumerate(arr):
        if v == key:
            return i
    return -1

def run_linear_search():
    results = []
    R = int(input("Enter the number of runs: "))
    for _ in range(R):
        n = int(input("Enter the number of elements: "))
        arr = list(map(int, input("Enter the elements of the array: ").split()))
        key = int(input("Enter the key element to be searched: "))
        start = time.time()
        for _ in range(10000):
            res = linear_search(arr, key)
        end = time.time()
        print(f"Key {key} {'found at position ' + str(res) if res != -1 else 'not found'}")
        print(f"Time taken to search key: {(end - start)*1000:.4f} ms\n")
        results.append((n, (end - start) * 1000))
    return results

def plot_results(results):
    plt.plot([r[0] for r in results], [r[1] for r in results], 'o-')
    plt.xlabel('Number of Elements (n)')
    plt.ylabel('Time Taken (ms)')
    plt.title('Linear Search Time Complexity')
    plt.grid(True)
    plt.show()

results = run_linear_search()
plot_results(results)
