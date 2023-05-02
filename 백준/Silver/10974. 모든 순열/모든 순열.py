n = int(input())
lst = []

def dfs():
    if len(lst) == n:
        print(*lst)
        return
    for i in range(1, n + 1):
        if i not in lst:
            lst.append(i)
            dfs()
            lst.pop()

dfs()