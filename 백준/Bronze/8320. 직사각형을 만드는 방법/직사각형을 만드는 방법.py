# 변의 길이가 1인 정사각형 n개를 가지고 있다. 이 정사각형을 이용해서 만들 수 있는 직사각형의 개수는 총 몇 개일까?

N = int(input())

ans = 0
for i in range(1, N+1):
    for j in range(i,N+1):
        if i * j <= N:
            ans += 1
print(ans)