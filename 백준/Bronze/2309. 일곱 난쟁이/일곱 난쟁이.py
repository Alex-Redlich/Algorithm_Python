# 일곱 난쟁이가 아닌 애들 찾기, 9명중에 2명을 찾으면 된다.
# 난쟁이의 키의 합은 100, 그럼 전체 더한것에 100을 빼면 그 두명의 합이 나온다
# 2중 포문을 이용해서 2명의 합이 같을때 둘을 빼주자
# 오름차순 한 배열에서 둘을 빼면서 프린트하면 정답

N = 9
arr = [int(input()) for _ in range(9)]
arr.sort()
result = 0
num = sum(arr) - 100
a = 0
b = 0
for i in range(N-1):
   for j in range(i+1, N):
       if arr[i] + arr[j] == num:
           a = arr[i]
           b = arr[j]

for i in arr:
    if i != a and i != b:
        print(i)

