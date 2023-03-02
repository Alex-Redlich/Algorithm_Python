# 암호 코드 (앞 쪽 0은 무시)
# 참고 -> dict의 key는 mutable 불가능
P = {(2, 1, 1): 0,
     (2, 2, 1): 1,
     (1, 2, 2): 2,
     (4, 1, 1): 3,
     (1, 3, 2): 4,
     (2, 3, 1): 5,
     (1, 1, 4): 6,
     (3, 1, 2): 7,
     (2, 1, 3): 8,
     (1, 1, 2): 9}
 
# 암호 코드 정보 확인 (16진수 -> 2진수)
hex_to_bin = {'0': [0, 0, 0, 0],
              '1': [0, 0, 0, 1],
              '2': [0, 0, 1, 0],
              '3': [0, 0, 1, 1],
              '4': [0, 1, 0, 0],
              '5': [0, 1, 0, 1],
              '6': [0, 1, 1, 0],
              '7': [0, 1, 1, 1],
              '8': [1, 0, 0, 0],
              '9': [1, 0, 0, 1],
              'A': [1, 0, 1, 0],
              'B': [1, 0, 1, 1],
              'C': [1, 1, 0, 0],
              'D': [1, 1, 0, 1],
              'E': [1, 1, 1, 0],
              'F': [1, 1, 1, 1]}
 
T = int(input())
for tc in range(1, T+1):
    # N: 세로, M: 가로
    N, M = map(int, input().split())
    arr = [[] for _ in range(N)]
     
    # 16진수 -> 2진수 변환 후 배열 입력
    for i in range(N):
        tmp = input()
        for j in range(M):
            arr[i] += hex_to_bin[tmp[j]]
     
    # 2진수 -> 암호코드 변환
    def scanner():
        ans = 0
        # 하나의 row씩 체크하며
        for i in range(N):
            # 16진수 -> 2진수 -> 16진수의 최댓값 F는 2진수로 1111 -> 4bit
            # 인덱스 에러 방지를 위해 -1 (마지막 제외)
            j = M * 4 - 1
            # 최소 가로 길이(56 -> 마지막 55)
            while j >= 55:
                # 현재가 1이고 이전이 0 (연속된 1의 개수를 count하기 위함)
                if arr[i][j] and arr[i-1][j] == 0:
                    pwd = []
                     
                    # 모든 암호코드는 8개의 숫자로 구성 -> 체크
                    for _ in range(8):
                        # 암호는 (
                        # 암호 코드는 오른쪽 3개의 숫자만 봐도 됨(가장 앞은 x)
                        c2 = c3 = c4 = 0
                        # 0이면 -> 하나 앞으로
                        while arr[i][j] == 0:
                            j -= 1
                        # 1이면 -> 하나 앞으로 & c4(1개수) count += 1
                        while arr[i][j] == 1:
                            c4, j = c4 + 1, j - 1
                        # 0이면 -> 하나 앞으로 & c3(0개수) count += 1
                        while arr[i][j] == 0:
                            c3, j = c3 + 1, j - 1
                        # 1이면 -> 하나 앞으로 & c2(1개수) count += 1
                        while arr[i][j] == 1:
                            c2, j = c2 + 1, j - 1
 
                        # 최솟값 찾고  -> why? 1:3:1:2 이렇게 주어질 수도 있지만
                        # 2:6:2:4 -> 이렇게 주어질 수도 있음 -> 최솟값인 2로 나눠야
                        # 원하는 값을 얻을 수 있다.
                        MIN = min(c2, c3, c4)
                        # 최솟값으로 나눠서 암호문에 대응하는 숫자 찾기
                        # 비율이기 때문에 가장 작은 값으로 나눠주는 과정 필요
                        pwd.append(P[(c2 // MIN, c3 // MIN, c4 // MIN)])
                     
                    # 짝수 & 홀수 자리 합
                    even_digit_sum = pwd[0] + pwd[2] + pwd[4] + pwd[6]
                    odd_digit_sum = pwd[1] + pwd[3] + pwd[5] + pwd[7]
 
                    #  (홀수 자리의 합 x 3) + 짝수 자리의 합 + 검증 코드가 10의 배수
                    if (odd_digit_sum * 3 + even_digit_sum) % 10 == 0:
                        ans += odd_digit_sum + even_digit_sum
                # 한 칸 앞으로
                j -= 1
        return ans
    print('#{} {}'.format(tc, scanner()))
''' 
틀린 내 풀이.. 
code = {(2,1,1) : '0',
        (2,2,1) : '1',
        (1,2,2) : '2',
        (4,1,1) : '3',
        (1,3,2) : '4',
        (2,3,1) : '5',
        (1,1,4) : '6',
        (3,1,2) : '7',
        (2,1,3) : '8',
        (1,1,2) : '9'}

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    arr = list(set(input() for _ in range(N)))
    arr = sorted(arr)[1:]
    sc_code = []
    real_answer = []
    sc_code_list = []

    for i in arr:
        binary = '0' + str(bin(int(i,16))).lstrip('0b')

        n1 = n2 = n3 = 0
        cnt = 0
        result = ''
        for j in range(len(binary)):
            if binary[j] == '1' and n2 == 0 and n3 == 0:
                n1 += 1
            elif binary[j] == '0' and n1 > 0 and n3 == 0 :
                n2 += 1
            elif binary[j] == '1' and n1 > 0 and n2 > 0:
                n3 += 1
            elif n3 != 0 :
                cnt += 1
                r = min(n1,n2,n3)
                temp = code[(n1//r, n2//r, n3//r)]
                result += temp
                if cnt == 8:
                    sc_code.append(result)
                    result = ''
                    n1 = n2 = n3 = 0
                else:
                    n1 = n2 = n3 = 0

        for n in range(len(sc_code)):
            sc_code_list.append([int(a) for a in sc_code[n]])


    even = 0
    odd = 0
    for j in range(len(sc_code)):
        for k in range(8):
            if k % 2:
                even += sc_code_list[j][k]
            else:
                odd += sc_code_list[j][k]
        if (odd*3 + even) % 10 == 0:
            real_answer.append(sum(sc_code_list[j]))
            even = odd = 0
        else:
            real_answer.append(0)
            even = odd = 0



    print(f'#{tc} {real_answer[0]}')
'''




