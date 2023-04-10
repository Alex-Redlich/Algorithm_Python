n = int(input())
A = set(map(int,input().split()))
M = int(input())
arr = list(map(int,input().split()))

for num in arr:
    if num in A:
        print(1)
    else:
        print(0)