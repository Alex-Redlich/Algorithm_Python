T = 10
for test_case in range(1, T + 1):
    _ = int(input())
    N = 100
    arr = [list(map(int, input().split())) for _ in range(N)]  # N*N 배열에 입력값 넣기
 
    ans = s3 = s4 = 0
    for i in range(N):
        s1 = s2 = 0
        for j in range(N):
            s1 += arr[i][j]  # 가로
            s2 += arr[j][i]  # 세로
        ans = max(ans, s1, s2)  # 맥스값 계산
 
        s3 += arr[i][i]  # 대각선
        s4 += arr[i][N-1-i]  # 왼쪽 대각선
    ans = max(ans, s3, s4)
 
    print(f'#{test_case} {ans}')