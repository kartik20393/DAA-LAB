import sys

def minKey(key, mstSet):
    min_value = sys.maxsize
    min_index = -1
    for v, (k, mst) in enumerate(zip(key, mstSet)):
        if not mst and k < min_value:
            min_value, min_index = k, v
    return min_index

def printMST(parent, c):
    total_weight = 0
    print("Edge\tWeight")
    for i in range(1, len(parent)):
        weight = c[i][parent[i]]
        total_weight += weight
        print(f"{parent[i]+1} - {i+1}\t{weight}")
    print("Total cost of the minimum spanning tree:", total_weight)

def primMST(c):
    n = len(c)
    parent = [-1] * n
    key = [sys.maxsize] * n
    mstSet = [False] * n
    key[0] = 0

    for _ in range(n):
        u = minKey(key, mstSet)
        mstSet[u] = True
        for v in range(n):
            if c[u][v] > 0 and not mstSet[v] and c[u][v] < key[v]:
                parent[v] = u
                key[v] = c[u][v]

    printMST(parent, c)

# Main code
n = int(input("Enter the number of vertices: "))
print("Enter the adjacency matrix row by row, with values separated by spaces:")
c = [list(map(int, input().split())) for _ in range(n)]
primMST(c)
