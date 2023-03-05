def toPos(st):
    return int(st[1]), ord(st[0])-ord('A')+1

def toAB(i,j):
    return chr((j-1)+ord('A'))+str(i)

K, S, N = input().split()
# 킹, 돌의 위치를 좌표로 변환
ci, cj = toPos(K)
si, sj = toPos(S)
N = int(N)
dct = {'R':(0,1), 'L':(0,-1),'B':(-1,0),'T':(1,0),'RT':(1,1),'LT':(1,-1),'RB':(-1,1),'LB':(-1,-1)}
for _ in range(N):
    di,dj = dct[input()]
    ni,nj = ci+di, cj+dj
    if 1<=ni<=8 and 1<=nj<=8:           # 범위내
        if (ni,nj)==(si,sj):            # 이동할 위치에 돌이 있는 경우
            ei,ej = si+di, sj+dj        # 돌의 이동할 위치
            if 1<=ei<=8 and 1<=ej<=8:   # 돌 이동가능
                si,sj = ei,ej
                ci,cj = ni,nj
        else:
            ci, cj = ni, nj

print(toAB(ci,cj), toAB(si,sj), sep='\n')