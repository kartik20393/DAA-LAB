INF = 99999

def printSolution(V, D):
    print("The following matrix shows the shortest distances between every pair of vertices")
    for row in D:
        print("".join(f"{'INF':>7}" if val == INF else f"{val:7d}" for val in row))

def floyd(V, C):
    D = [row[:] for row in C]
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if D[i][j] > D[i][k] + D[k][j]:
                    D[i][j] = D[i][k] + D[k][j]
    printSolution(V, D)

V = int(input("Enter the number of vertices: "))
C = [list(map(int, input("Enter row with space-separated costs: ").split())) for _ in range(V)]
floyd(V, C)
