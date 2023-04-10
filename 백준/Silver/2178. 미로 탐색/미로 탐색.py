from collections import deque

N, M = map(int,input().split())
arr = [list(map(int,input())) for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append(((x,y)))

    while queue:
        x,y = queue.popleft()

        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]

            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1:
                queue.append((nx,ny))
                arr[nx][ny] = arr[x][y] + 1
    return arr[N-1][M-1]

print(bfs(0,0))
