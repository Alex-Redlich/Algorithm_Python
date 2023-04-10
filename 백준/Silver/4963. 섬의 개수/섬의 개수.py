from collections import deque

def bfs(x,y):
    dx = [-1, -1, -1, 0, 1, 1, 1, 0]
    dy = [-1, 0, 1, 1, 1, 0, -1, -1]
    queue = deque()
    queue.append((x,y))
    arr[x][y] = 0
    while queue:
        x,y = queue.popleft()
        for dir in range(8):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 <= nx < H and 0 <= ny < W and arr[nx][ny] == 1:
                arr[nx][ny] = 0
                queue.append((nx,ny))
    return

while True:
    W, H = map(int, input().split())
    if W == 0 and H == 0:
        break
    cnt = 0
    arr = [list(map(int, input().split())) for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if arr[i][j] == 1:
                bfs(i,j)
                cnt += 1
    print(cnt)




