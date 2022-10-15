from collections import deque

def main():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        A = []
        for __ in range(n):
            A.append(list(map(int, input().split())))
        
        max_val = float("-inf")
        for i in range(n):
            for j in range(m):
                if A[i][j] > max_val:
                    max_val = A[i][j]
        
        queue = deque()
        visited = [[0] * m for i in range(n)]
        for i in range(n):
            for j in range(m):
                if A[i][j] == max_val:
                    queue.append((i, j, 0))
                    visited[i][j] = 1
        dir = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        
        result = 0
        while len(queue):
            x, y, t = queue.popleft()
            result = max(result, t)
            for X, Y in dir:
                if not (0 <= x + X < n and 0 <= y + Y < m):
                    continue
                if visited[x + X][y + Y]:
                    continue
                visited[x + X][y + Y] = 1
                queue.append((x + X, y + Y, t + 1))

        print(result)

if __name__ == "__main__":
    main()
