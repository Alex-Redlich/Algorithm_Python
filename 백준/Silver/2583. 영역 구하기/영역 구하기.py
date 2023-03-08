# BFS로 풀기

from collections import deque

M, N, K = map(int, input().split())
arr = [[0] * N for _ in range(M)]
# 좌표값을 받아서 해당 부분 다 1로 바꾸기
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1,y2):
            arr[j][i] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]  # 델타 탐색 이용

def bfs(x, y):  # BFS 이용해서 델타 탐색하면서 0인부분 카운트해서 1로 바꾸고, 카운팅 다하면 result에 넣기
    queue = deque()
    queue.append((x, y))
    arr[x][y] = 1
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and arr[nx][ny] == 0:
                arr[nx][ny] = 1
                queue.append((nx, ny))
                cnt += 1
    result.append(cnt)


result = []
for i in range(M):
    for j in range(N):
        if arr[i][j] == 0:  # 0인곳 찾아서 BFS 돌리기
            bfs (i, j) # (0,0) = 7 (0,6) = 13 (4,0) = 1

result.sort()
print(len(result))
print(*result)