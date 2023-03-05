arr = [list(map(int,input().split())) for _ in range(5)]

lst = []

for _ in range(5):
    lst += list(map(int, input().split()))

pos_lst = [0] * 26
for i in range(5):
    for j in range(5):
        pos_lst[arr[i][j]] = (i,j)


v = [[0]*10 for _ in range(4)]
for n in lst:
    i, j = pos_lst[n]
    v[0][j] += 1
    v[1][i] += 1
    v[2][i-j] += 1
    v[3][i+j] += 1

    cnt = 0
    for tlst in v:
        cnt += tlst.count(5)
    if cnt >= 3:
        break

print(sum(v[0]))