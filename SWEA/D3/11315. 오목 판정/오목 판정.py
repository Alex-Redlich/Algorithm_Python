# 대각선 포함이라서 8방향 인것 같지만??
# 4방향만 봐도 될것같은데??
# 우하 <> 좌상 , 우 <> 좌 , 하 <> 상 , 좌하 <> 우상
dr = [0, 1, 1, 1]
dc = [1, 1, 0, -1]


# 내가 다음 위치를 계산했을때 해당 위치가 유효범위 안에 있는지(2차원 배열의 크기를)
def is_valid(r, c):
    return 0 <= r < N and 0 <= c < N


def solve():
    # 전체 위치 r,c 에대해서 오목 판별
    for r in range(N):
        for c in range(N):
            # 현재 r,c 위치에 돌이 있어야 오목판별 가능
            if arr[r][c] == "o":
                # 4방향으로 최대 5칸까지 가봐야 한다.
                for d in range(4):
                    for l in range(5):
                        # 다음 방향 d 방향으로 l칸 만큼 이동
                        nr = r + dr[d] * l
                        nc = c + dc[d] * l
                        # 계산한 nr, nc가 2차원 배열 범위 안인지 확인
                        # 만약 범위 밖이면 탐색 중단
                        # 그 위치로 갔더니 돌이 아니면 탐색 중단
                        if not is_valid(nr, nc) or arr[nr][nc] == ".":
                            break
                    # 중간에 break 한적이 없다 ==>
                    # 현재 방향으로 5칸을 완성 했다는 의미
                    else:
                        # 바로 함수 종료 해버리기
                        return "YES"

    # 끝까지 탐색 했는데 오목을 찾지 못한 경우
    return "NO"


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    arr = [list(input()) for _ in range(N)]

    print(f"#{tc} {solve()}")