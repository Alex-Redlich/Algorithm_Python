# N = 사람 수 M = 걸리는 시간(초) K = 붕어빵 개수
T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = sorted(list(map(int, input().split())))
    
    result = 'Possible'

    sold = 0
    for i in arr:
        made = (i // M) * K

        spare = made - sold

        if spare <= 0:
            result = 'Impossible'
            break
        else:
            sold += 1
    print(f'#{tc} {result}')

