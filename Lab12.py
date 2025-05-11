MAX = 100
C = [[0]*MAX for _ in range(MAX)]
Visited = [0]*MAX
Queue = [0]*MAX

def BFS(V, n):
    front, rear = 0, 0
    Visited[V] = 1
    Queue[rear] = V
    while front <= rear:
        V = Queue[front]
        front += 1
        print(f"{V} ", end="")
        for I in range(1, n+1):
            if C[V][I] == 1 and not Visited[I]:
                rear += 1
                Queue[rear] = I
                Visited[I] = 1

if __name__ == "__main__":
    n = int(input("Enter the number of vertices in the graph: "))
    print("Enter the cost matrix of the graph:")
    for i in range(1, n+1):
        C[i][1:n+1] = list(map(int, input().split()))
    V = int(input("Enter the starting vertex: "))
    print("BFS traversal of the graph is: ", end="")
    BFS(V, n)
