# 이렇게 러시아 국기 같은 깃발을 만들기 위해서 새로 칠해야 하는 칸의 개수의 최솟값을 구하여라.
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    min_ = N*M

    W_cnt = 0
    for w in range(0,N-2):
        for k in range(M):
            if arr[w][k] != 'W':
                W_cnt += 1

        B_cnt = 0
        for b in range(w+1, N-1):
            for k in range(M):
                if arr[b][k] != 'B':
                    B_cnt += 1

            R_cnt = 0
            for r in range(b+1, N):
                for k in range(M):
                    if arr[r][k] != 'R':
                        R_cnt += 1

            total = W_cnt + B_cnt + R_cnt
            if min_ > total:
                min_ = total
    print(f'#{tc} {min_}')

