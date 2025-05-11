def warshall(c, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                c[i][j] = c[i][j] or (c[i][k] and c[k][j])
    print("The transitive closure of the graph is:")
    for row in c:
        print(' '.join(map(str, row)))

def main():
    n = int(input("Enter the number of vertices: "))
    c = []
    print("Enter the adjacency matrix:")
    for _ in range(n):
        c.append(list(map(int, input().split())))
    warshall(c, n)

if __name__ == "__main__":
    main()
