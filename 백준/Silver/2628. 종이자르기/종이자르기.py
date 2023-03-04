h, v = map(int, input().split())
N = int(input())
h_lst = [0, h]
v_lst = [0, v]
for n in range(N):
    dir, num = map(int, input().split())
    if dir == 0 :
        v_lst.append(num)
    else:
        h_lst.append(num)

v_lst.sort()
h_lst.sort()

v_max = 0
for i in range(1, len(v_lst)):
    v_max = max(v_max, v_lst[i]-v_lst[i-1])

h_max = 0
for j in range(1, len(h_lst)):
    h_max = max(h_max, h_lst[j]-h_lst[j-1])

result = v_max * h_max

print(result)

