from collections import deque

def turn(dir):
    global direction
    if dir == 'L':
        direction = (direction - 1) % 4  # (0 - 1) % 4 = 3
    else:
        direction = (direction + 1) % 4

# 빈곳 0, 뱀 몸 1, 사과 2
n = int(input())
k = int(input())

# 어레이 만들기
arr = [[0 for _ in range(n)] for _ in range(n)]

# 사과 찍기
for _ in range(k):
    x, y = map(int, input().split())
    arr[x-1][y-1] = 2

# 초-방향 딕셔너리에 저장
dict_ = {}
l = int(input())
for _ in range(l):
    sec, dir = input().split()
    dict_[int(sec)] = dir
# 상(0) 우(1) 하(2) 좌(3)
dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

# 초기화
direction = 1  # 오른쪽부터
time = 1
snake = deque([[0, 0]])
x, y = 0, 0
arr[0][0] = 1

# 뱀 이동
while True:
    x, y = x + dx[direction], y + dy[direction]
    if 0 <= x < n and 0 <= y < n and arr[x][y] != 1:  # 벽 혹은 자신의 몸통이 아닐 때
        if not arr[x][y] == 2:  # 사과가 아닐 때
            tailX, tailY = snake.popleft()  # 꼬리 자르기
            arr[tailX][tailY] = 0
        arr[x][y] = 1  # 뱀 전진
        snake.append((x, y))  # 뱀 머리 위치 추가
        if time in dict_.keys():  # 시간에 따라 방향 값이 있는지 확인
            turn(dict_[time])
        time += 1
    else:  # 벽을 만났거나, 자신의 몸통을 만났을 때
        print(time)
        break