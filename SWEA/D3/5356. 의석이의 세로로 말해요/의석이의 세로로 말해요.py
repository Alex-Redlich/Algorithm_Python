# 세로로 읽기, 전치행렬(같은 길이의 배열일때만 가능)
# 하나하나 루프를 돌면서 받아와야된다

T = int(input())
for tc in range(1,T+1):
    arr = [input() for _ in range(5)]
    result = ''
    for j in range(15):
        for i in range(5):
            if j < len(arr[i]):
                result += arr[i][j]
    
    print(f'#{tc} {result}')