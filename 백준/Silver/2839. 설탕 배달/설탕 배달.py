N = int(input())
# 최소개수 => 5킬로 봉투를 최대한 사용, 3킬로만 사용할 수도 있으니
# N//5 ~ 0까지 루프
for cnt_5 in range(N//5, -1, -1):
    cnt_3 = (N-cnt_5*5)//3          # 5킬로 봉투량 뺀 무게를 3킬로 봉지수로 계산
    if cnt_5*5 + cnt_3*3 == N:      # 정답 찾음
        print(cnt_5+cnt_3)
        break
else:                               # 떨어지는 숫자를 찾지못한 경우: -1
    print(-1)