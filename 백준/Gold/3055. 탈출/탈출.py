from collections import deque

# 물 퍼지기
def flood():
    # 빈 리스트 하나 만들어서, 물인 곳 찾아서 넣기
    water = []
    for i in range(R):
        for j in range(C):
            if arr[i][j] == "*" and not visited[i][j]:
                water.append((i, j))
                visited[i][j] = True
    # 물이 차있는 부분 먼저 4방향으로 늘리기
    for x, y in water:
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 방문처리를 함으로써 다음 사이클때 물이 중복으로 퍼지지 않도록 조건 설정
            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]:
                if arr[nx][ny] == ".":
                    arr[nx][ny] = "*"

# 고슴도치 움직이기
def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    cnt = 0

    while queue:
        cnt += 1 # 사이클 도는 것 체크하면서 도착지까지 가는 시간 구하기

        flood() # 사이클에 맞춰서 물 퍼지기

        for _ in range(len(queue)):
            x, y = queue.popleft()

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]:
                    if arr[nx][ny] == ".":
                        queue.append((nx, ny))
                        visited[nx][ny] = True
                    elif arr[nx][ny] == "D":
                        return cnt

    return "KAKTUS"

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 고슴도치 위치 찾기
sx, sy = 0, 0
for i in range(R):
    for j in range(C):
        if arr[i][j] == "S":
            sx, sy = i, j # 찾았으면 빈공간으로 바꿔야 물이 들어간다
            arr[i][j] = "."

print(bfs(sx, sy))