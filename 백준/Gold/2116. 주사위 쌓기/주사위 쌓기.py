Can_choice={1:(2,3,4,5),2:(1,3,5,6),3:(1,2,4,6),
            4:(1,3,5,6),5:(1,2,4,6),6:(2,3,4,5)}
back={1:6,2:4,3:5,4:2,5:3,6:1}

import sys
sys.setrecursionlimit(10**5)
input=sys.stdin.readline
dice_num=int(input())
dice=[[0,0,0,0,0,0]]+[list(map(int,input().split())) for _ in range(dice_num)]
max_sum=0
def choice(k,down,cnt):
    global max_sum
    if k==dice_num+1:
        max_sum=max(max_sum,cnt)
    else:
        idx=dice[k].index(down)+1
        up=back[idx]
        cnt+=max([dice[k][i-1] for i in Can_choice[up]])
        choice(k+1,dice[k][up-1],cnt)

for i in range(1,7):
    choice(2,dice[1][i-1],max([dice[1][i-1] for i in Can_choice[i]]))
print(max_sum)