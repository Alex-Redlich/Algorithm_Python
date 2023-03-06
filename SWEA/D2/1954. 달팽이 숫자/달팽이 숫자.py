T = int(input())
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]  # 순서는 우 하 좌 상
for test_case in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]  # 0으로 차있는 배열 생성
 
    i, j, cnt, dr = 0, 0, 1, 0 # 초기화
    arr[i][j] = cnt  # (0,0)에서 시작 1넣고 시작
    cnt += 1
 
    while cnt <= N*N:  # 카운트가 다 다를때까지
        ni, nj = i+di[dr], j+dj[dr]  # 오른쪽부터 방향 순회
        if 0<=ni<N and 0<=nj<N and arr[ni][nj]==0:  # 범위설정
            i, j = ni, nj
            arr[i][j]=cnt
            cnt+=1
        else:
            dr = (dr+1)%4  # 방향 초기화
 
    print(f'#{test_case}')
    for lst in arr:
        print(*lst)