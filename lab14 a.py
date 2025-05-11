def main():
    n = int(input("Enter the number of vertices: "))
    c = [list(map(int, input("Enter row {}: ".format(i+1)).split())) for i in range(n)]
    indeg = [sum(c[i][j] != 0 for i in range(n)) for j in range(n)]
    flag = [0] * n
    count = 0

    print("The topological order is:")
    while count < n:
        for k in range(n):
            if indeg[k] == 0 and not flag[k]:
                print(f"{k+1:3}", end='')
                flag[k] = 1
                count += 1
                for i in range(n):
                    if c[k][i] != 0:
                        indeg[i] -= 1
    print()

if __name__ == "__main__":
    main()
