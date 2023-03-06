T = 10
for test_case in range(1, T + 1):
    _ = int(input())
    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]
 
    # [1] 2값인 시작위치 찾기(ci, cj)
    ci = 99
    for j in range(100):
        if arr[ci][j] == 2:
            cj = j
            break
 
    # [2] 0행까지 올라가면서 1. (좌/우), 2. 위
    while ci>0:
        arr[ci][cj] = 0
        if arr[ci][cj-1] == 1:  # 왼쪽에 길
            cj -= 1
        elif arr[ci][cj+1] == 1: # 오른쪽에 길
            cj += 1
        else:
            ci -= 1
 
    print(f'#{test_case} {cj-1}')