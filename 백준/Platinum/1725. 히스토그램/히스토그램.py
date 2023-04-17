import sys
input = sys.stdin.readline

n = int(input())
arr = []
result = 0
left = 0
for _ in range(n):
    arr.append(int(input()))
arr.append(0)
stack = [(0, arr[0])]

for i in range(1,n+1):
    left = i
    while stack and stack[-1][1] > arr[i]:
        left, temp = stack.pop()
        result = max(result, temp*(i-left))
    stack.append((left, arr[i]))

print(result)