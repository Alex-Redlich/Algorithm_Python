N = int(input())
lst = []
for _ in range(N):
    x,y = map(int,input().split())
    lst.append([x,y])

lst.sort(key=lambda x : (x[0],x[1]))
for i in range(N):
    print(lst[i][0], lst[i][1])