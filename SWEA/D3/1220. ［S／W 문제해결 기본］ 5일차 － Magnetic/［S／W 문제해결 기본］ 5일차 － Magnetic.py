# 시간이 흐른 뒤에 자성체들이 서로 충돌하여 테이블 위에 남아있는 교착 상태의 개수를 구하라.
for tc in range(1,11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    for i in range(N):
        r, c = 0, i  # 열 계산
        stack = []
        while r < N :  # 모든 행을 도는 동안
            if not stack and arr[r][c] == 1:  # N 극일때, 스택이 비어있지 않는다면 
                # 스택이 차있다면 굳이 넣어서 계산 복잡하게 하지말기
                stack.append(1)  # 좌표값이 필요한게 아니라서 숫자용으로 활용
            elif stack and arr[r][c] == 2:  # 스택이 차있고, S극이라면(스택안은 N극만 있음)
                cnt += stack.pop()  # pop해서 더해주기(1씩 증가)
            r += 1  # 다음 행 으로 가기

    print(f'#{tc} {cnt}')