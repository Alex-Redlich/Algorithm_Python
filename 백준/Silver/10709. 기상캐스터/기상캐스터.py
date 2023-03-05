H, W = map(int,input().split())
arr = [input() for _ in range(H)]
v = [[0]*W for _ in range(H)]
for i in range(H):
    cnt = -1
    for j in range(W):
        if arr[i][j] == 'c':
            cnt = 0
        else:
            if cnt >= 0:
                cnt += 1
        v[i][j] = cnt

for lst in v:
    print(*lst)