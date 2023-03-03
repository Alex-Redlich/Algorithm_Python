# 농장의 크기 N와 농작물의 가치가 주어질 때, 규칙에 따라 얻을 수 있는 수익은 얼마인지 구하여라.
# 접근 방법 : 마름모를 어떻게 만들지?
# 0) 시작점은 N의 중간 mid 변수 사용
# 1) start, end 변수 사용해서 
# 2) 한줄씩 검사하는데 start, end 에 1씩 더하고 빼서 길이를 점점 늘리기
# 3) 열이 mid가 되면 반대로 계산하기

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    result = 0
    mid = N//2
    start = end = mid
    for i in range(N):
        for j in range(start, end+1):
            result += arr[i][j]
        if i < mid :
            start,end = start-1, end+1
        else:
            start,end = start+1, end-1

    print(f'#{tc} {result}')