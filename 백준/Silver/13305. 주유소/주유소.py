N = int(input())
arr = list(map(int,input().split()))
cost = list(map(int,input().split()))

res = 0
m = cost[0]
for i in range(N-1):
    if cost[i] < m :
        m = cost[i]
    res += m*arr[i]

print(res)