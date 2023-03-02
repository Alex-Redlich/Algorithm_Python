# 한 번에 잡을 수 있는 최대 파리수를 출력하라.

T = int(input())
for tc in range(1,T+1):
    dx = [0, 1, 0, -1]  # 십자가 모양
    dy = [1, 0, -1, 0]
    dx_2 = [-1, 1, 1, -1]  # X 모양
    dy_2 = [1, 1, -1, -1]
    total = 0
    result = 0
    N, M = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]  # 배열 생성

    for x in range(N):
        for y in range(N):
            cnt1 = arr[x][y]  # 가장 가운데 값을 저장
            cnt2 = arr[x][y]  # cnt1 = + 모양 cnt2 = X 모양
            for k in range(4):  # 4방향 반복
                for l in range(1,M):  # 분사세기
                    nx = x + dx[k]*l
                    ny = y + dy[k]*l
                    nx_2 = x + dx_2[k]*l
                    ny_2 = y + dy_2[k]*l

                    if 0 <= nx < N and 0 <= ny < N:  # 범위에 맞다면
                        cnt1 += arr[nx][ny]  # 해당 파리의 값을 더해줌
                    if 0 <= nx_2 < N and 0 <= ny_2 < N:
                        cnt2 += arr[nx_2][ny_2]

            total = max(cnt1, cnt2)  # 2개 모양중 더 큰 값으로
            if total > result :  # 최대값 찾기
                result = total

    print(f'#{tc} {result}')



