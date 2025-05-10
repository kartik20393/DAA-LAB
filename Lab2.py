import time
import matplotlib.pyplot as plt

def binary_search(arr, key):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def main():
    R = int(input("Enter the number of runs: "))
    N_values, Times = [], []
    for _ in range(R):
        n = int(input("Enter the number of elements: "))
        arr = sorted(map(int, input("Enter the elements of an array: ").split()))
        key = int(input("Enter the key element to be searched: "))
        repeat = 10000
        start = time.time()
        for _ in range(repeat):
            binary_search(arr, key)
        end = time.time()
        N_values.append(n)
        Times.append((end - start) * 1000)
        print(f"Key {key} {'found' if binary_search(arr, key) != -1 else 'not found'} at position {binary_search(arr, key)}")
    plt.plot(N_values, Times, 'o-')
    plt.xlabel('Number of Elements (n)')
    plt.ylabel('Time Taken (milliseconds)')
    plt.title('Binary Search Time Complexity')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
