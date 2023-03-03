N = int(input())
arr = [[0] * 1002 for _ in range(1002)]
for n in range(1,N+1):
    x,y,h,v = map(int, input().split())
    for i in range(x,x+h):
        for j in range(y,y+v):
            arr[i][j] = n
            
cnt_lst = [0] * (N+1)
for n in range(1, N+1):
    for i in range(1002):
        for j in range(1002):
            if arr[i][j] == n:
                cnt_lst[n] += 1

for x in range(1,N+1):
    print(cnt_lst[x])