# 입력 받기
n = int(input()) 
arr = list(map(int, input().split())) 

# 어레이 정렬하기 꼭
arr.sort()

# 투 포인터 알고리즘
x = int(input()) 
start, end = 0, n-1 
count = 0 

while start < end:
    if arr[start] + arr[end] < x:
        start += 1
    elif arr[start] + arr[end] > x:
        end -= 1
    else:
        count += 1
        start += 1
        end -= 1


print(count)
