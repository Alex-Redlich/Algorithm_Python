from collections import deque

T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())
    queue = deque(list(map(int, input().split())))
    count = 0
    while queue:
        max_ = max(queue)
        First = queue.popleft()
        M -= 1

        if max_ == First:
            count += 1
            if M < 0:
                print(count)
                break

        else:
            queue.append(First)
            if M < 0 :
                M = len(queue) - 1
