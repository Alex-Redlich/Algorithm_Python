T = int(input())
di, dj = (1, -1, 0, 0), (0, 0, -1, 1)   # 상/하/좌/우
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for i in range(len(arr)):   # 좌표 X2처리(0.5이동 대신)
        arr[i][0] *= 2
        arr[i][1] *= 2
    ans = 0

    for _ in range(4001):
        # [1] 1칸 이동
        for i in range(len(arr)):
            arr[i][0]+=dj[arr[i][2]]
            arr[i][1]+=di[arr[i][2]]

        # [2] 같은좌표 찾기(중복되면 삭제셋에 추가)
        v, ddel = set(), set()
        for i in range(len(arr)):
            cj, ci = arr[i][0], arr[i][1]
            if (cj,ci) in v:    # 이미 있는 좌표(중복)
                ddel.add((cj,ci))
            else:
                v.add((cj,ci))

        # [3] 삭제후보 및 좌표를 벗어난경우 삭제
        for i in range(len(arr)-1, -1, -1):
            if (arr[i][0],arr[i][1]) in ddel:
                ans += arr[i][3]
                arr.pop(i)
            elif max(abs(arr[i][0]), abs(arr[i][1]))>2000:
                arr.pop(i)

        if len(arr)<2:
            break

    print(f'#{test_case} {ans}')