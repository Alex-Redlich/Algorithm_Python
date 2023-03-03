N = int(input())
arr = [[0] * 1001 for _ in range(1001)]
for n in range(1,N+1):
    x,y,h,v = map(int, input().split())
    for i in range(x,x+h):
        for j in range(y,y+v):
            arr[i][j] = n

cnt_lst = [0] * (N+1)
for lst in arr:
    for n in lst:
        cnt_lst[n] += 1
        
print(*cnt_lst[1:], sep='\n')



