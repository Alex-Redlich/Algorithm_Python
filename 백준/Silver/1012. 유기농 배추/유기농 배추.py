from collections import deque


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]

            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1:
                arr[nx][ny] = 0
                queue.append((nx,ny))
    return



T = int(input())
for tc in range(1,T+1):
    N, M, K = map(int,input().split())
    # 시작 배열 만들기
    arr = [[0] * M for _ in range(N)]
    for _ in range(K):
        x,y = map(int,input().split())
        arr[x][y] = 1

    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    cnt = 0
    # 시작 점 찾기
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                sx,sy = i,j
                bfs(sx,sy)
                cnt +=1

    print(cnt)