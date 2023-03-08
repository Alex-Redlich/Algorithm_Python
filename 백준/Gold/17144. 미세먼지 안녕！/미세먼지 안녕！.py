R, C, T = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(R)]

# 공기청정기 위치 찾기

for i in range(R):
    if arr[i][0] == -1:
        top = i
        bottom = i + 1
        break

# 먼지 확산하기
def dust_spread():
    dx = (-1,1,0,0)
    dy = (0,0,-1,1)
    # 확산되고 빠지는 먼지 받기 위한 어레이 생성
    spread = [[0] * C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            # 빈곳이나 공기청정기 위치는 지나가기
            if arr[i][j] == 0 or arr[i][j] == -1:
                continue
        
            dust = arr[i][j] // 5

            for k in range(4):
                ni, nj = i + dx[k], j + dy[k]
                # 조건에 맞춰서 4방향 더해주고, 가운데 빼주고
                if 0 <= ni < R and 0 <= nj < C and arr[ni][nj] != -1:
                    spread[ni][nj] += dust
                    spread[i][j] -= dust

    for i in range(R):
        for j in range(C):
            arr[i][j] += spread[i][j]  # 기존 값에다가 변경된 먼지 값 넣어주기


def clean_up():
    dx = (0,-1,0,1) # 반시계방향
    dy = (1,0,-1,0)
    x = top  # 위 공기청정기 시작
    y = 1
    dir = 0
    previous = 0

    while True:
        ni, nj = x + dx[dir], y + dy[dir]

        if x == top and y == 0:  # 공기청정기 도착하면 멈추기
            break
        if not 0 <= ni < R or not 0 <= nj < C:  # 범위 벗어나면 방향 바꾸기
            dir += 1
            continue

        arr[x][y], previous = previous, arr[x][y] # 한칸씩 밀어주기
        x, y = ni, nj

def clean_down():
    dx = (0,1,0,-1)  # 시계방향
    dy = (1,0,-1,0)
    x = bottom  # 아래 공기청정기 시작
    y = 1
    dir = 0
    previous = 0

    while True:
        ni, nj = x + dx[dir], y + dy[dir]

        if x == bottom and y == 0: # 공기청정기 도착하면 멈추기
            break
        if not 0 <= ni < R or not 0 <= nj < C: # 범위 벗어나면 방향 바꾸기
            dir += 1
            continue

        arr[x][y], previous = previous, arr[x][y] # 한칸씩 밀어주기
        x, y = ni, nj


for _ in range(T):  # 가동횟수만큼 함수들 실행
    dust_spread()
    clean_up()
    clean_down()

result = 2  #공기청정기 2칸 -1이니까 미리 2로 시작
for i in range(R):
    result += sum(arr[i])
print(result)