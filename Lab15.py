def sum_of_subsets(s, k):
    global count, w, x, d
    x[k] = 1
    if s + w[k] == d:
        count += 1
        print(f"InSubset {count} = ", end='')
        for i in range(k + 1):
            if x[i]:
                print(f"{w[i]} ", end='')
        print()
    else:
        if s + w[k] <= d and k + 1 < len(w):
            sum_of_subsets(s + w[k], k + 1)
        if s + w[k] + (w[k + 1] if k + 1 < len(w) else 0) <= d and k + 1 < len(w):
            x[k] = 0
            sum_of_subsets(s, k + 1)

def main():
    global w, x, count, d
    n = int(input("Enter the number of elements: "))
    w = [int(input(f"Enter element {i + 1}: ")) for i in range(n)]
    d = int(input("Enter the sum: "))
    total = sum(w)
    x = [0] * n
    count = 0
    if total < d or w[0] > d:
        print("No subset possible")
    else:
        sum_of_subsets(0, 0)

if __name__ == "__main__":
    main()
