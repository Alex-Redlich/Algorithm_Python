for _ in range(4):
    sj1,si1,ej1,ei1,sj2,si2,ej2,ei2 = map(int, input().split())
    if si1>ei2 or ei1<si2 or sj1>ej2 or ej1<sj2:    # 바깥쪽에 있는 경우
        ans = 'd'
    elif ej1==sj2 or sj1==ej2:   # 세로가 일치(붙어있는 경우)
        if ei1==si2 or si1==ei2:    # 가로가 일치(붙어있는 경우)
            ans = 'c'               # 점 (둘다 붙어있음)
        else:
            ans = 'b'               # 변 (하나만 붙어있음)
    elif ei1==si2 or si1==ei2:      # 세로X, 가로일치
        ans = 'b'
    else:
        ans = 'a'
    print(ans)