T = int(input())
for tc in range(1,T+1):
    arr = list(map(int, input().split()))[1:]
    cnt = 0
    for i in range(1,20):
        for j in range(0,i):
            if arr[i] < arr[j]:
                cnt += 1
    print(f'{tc} {cnt}')