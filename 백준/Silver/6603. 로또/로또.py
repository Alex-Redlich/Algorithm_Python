def dfs(len_, i):
    if len_ == 6:
        print(*result)
        return

    for i in range(i, K):
        if len_ + K - i < 6:
            return
        result.append(S[i])
        dfs(len_+1,i+1)
        result.pop()

while True:
    arr = list(map(int,input().split()))
    K = arr[0]
    S = arr[1:]
    if K == 0:
        break
    result = []
    dfs(0,0)
    print()