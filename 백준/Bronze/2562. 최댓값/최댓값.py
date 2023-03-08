lst = []
for _ in range(9):
    n = int(input())
    lst.append(n)
max_ = 0
max_idx = 0
for n in range(len(lst)):
    if max_ < lst[n]:
        max_ = lst[n]
        max_idx = n+1

print(max_)
print(max_idx)