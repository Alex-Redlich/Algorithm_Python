# 정사각형을 이어 붙인 넓이를 구하기
# 정사각형은 10 * 10으로 크기 고정

N = int(input())  # 색종이 갯수
arr = [[0]*101 for _ in range(101)]  # 100*100 0으로 가득찬 배열만들기
lst = [list(map(int,input().split())) for _ in range(N)]  # 해당 시작 좌표 받기

for x, y in lst:  # 좌표값을 넣어
    for i in range(x,x+10):  # 2중 포문 돌면서
        for j in range(y,y+10):
                arr[i][j] = 1  # 칠하고
result = 0
dx = [-1,0,1,0]
dy = [0,1,0,-1]  # 델타 탐색

for i in range(1,101):  # 2중포문으로 arr를 다 돌면서
    for j in range(1,101):
        if arr[i][j] == 1:  # 1이면
            cnt = 0
            for k in range(4):  # 4방향 탐색해서
                nx = i + dx[k]
                ny = j + dy[k]
                if arr[nx][ny] == 1:
                    cnt += 1  # 네 방향중 1인 경우 카운트
            if cnt == 3:  # 4면 중 3면이 1이면
                result += 1  # 테두리로 간주 1 결과 증가
            elif cnt == 2:  # 꼭지점이면
                result += 2  # 2 증가

print(result)
