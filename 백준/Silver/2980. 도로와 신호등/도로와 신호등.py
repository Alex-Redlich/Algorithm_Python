N, L = map(int, input().split())
# 시작지점과 목적지(L)을 포함해서 모든 신호등 위치 저장
arr = [[0,0,1]]+[list(map(int, input().split())) for _ in range(N)]+[[L,0,1]]

cnt = 0
for i in range(1, len(arr)):
    d, r, g = arr[i]
    # 지난 위치부터 현재위치의 차이(이동거리) 추가
    cnt += (d - arr[i-1][0])
    # 현재 신호등에서의 대기시간 추가
    # 신호등주기(r+g)로 나머지 구하면 => 진입시점
    # 진입시점이 r 보다 작으면 r시간이 끝날때까지 대기하므로 r - 진입시간
    cnt += max(0, r-(cnt%(r+g)))
print(cnt)