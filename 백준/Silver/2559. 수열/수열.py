'''
슬라이싱 사용하면 시간초과
N, K = map(int,input().split())
arr = list(map(int,input().split()))

max_ = []
for i in range(len(arr)):
    max_.append(sum(arr[i:i+K]))
print(max(max_))
'''

N, K = map(int, input().split())
lst = list(map(int, input().split()))

ans = sm = sum(lst[:K])
for i in range(K, N):
    # 바로 뒷자리를 추가, 제일 앞을 제거해서 연산을 최소화
    sm = sm + lst[i] - lst[i-K]
    ans = max(ans, sm)
print(ans)