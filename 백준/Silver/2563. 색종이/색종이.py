# 정사각형을 이어 붙인 넓이를 구하기
# 정사각형은 10 * 10으로 크기 고정

N = int(input())  # 색종이 갯수
arr = [[0]*100 for _ in range(100)]  # 100*100 0으로 가득찬 배열만들기
lst = [list(map(int,input().split())) for _ in range(N)]  # 해당 시작 좌표 받기
cnt = 0
for x, y in lst:  # 좌표값을 넣어
    for i in range(x,x+10):  # 2중 포문 돌면서
        for j in range(y,y+10):
            if arr[i][j] == 0:  # 칠해지지 않는 곳이라면
                arr[i][j] = 1  # 칠하고
                cnt += 1  # 1칸씩 추가

print(cnt)  # 모든 칸 추가 


