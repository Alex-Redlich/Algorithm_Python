T = 10
for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    ans = 100  # 최고점과 최저점의 차를 구하기 위한 변수
    for _ in range(N):
        lst.sort()  # 차순정렬
        lst[0] += 1  # 맨 앞에 한개 늘리고
        lst[-1] -= 1  # 바로 뒤에서 한개 줄이고 
        # 계속 반복하기
        if ans > max(lst)-min(lst):
            ans = max(lst)-min(lst)  # 최고점과 최저점의 차를 계산해서 계속 덮어주기
    print(f'#{test_case} {ans}')