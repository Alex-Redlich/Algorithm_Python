T = int(input())
for test_case in range(1, T+1):
    N, M, K = map(int, input().split())
    microbes = [list(map(int, input().split())) for _ in range(K)]
    # [세로, 가로, 미생물 수, 이동 방향]
    # [[1, 1, 7, 1], [2, 1, 7, 1], [5, 1, 5, 4], [3, 2, 8, 4], [4, 3, 14, 1], [3, 4, 3, 3], [1, 5, 8, 2], [3, 5, 100, 1], [5, 5, 1, 1]]

    answer = 0

    for time in range(M):
        merge = []
        for microbe in range(len(microbes)):
            # print(microbes)
            # (상: 1, 하: 2, 좌: 3, 우: 4)
            if microbes[microbe][3] == 1:
                microbes[microbe][0] -= 1
            elif microbes[microbe][3] == 2:
                microbes[microbe][0] += 1
            elif microbes[microbe][3] == 3:
                microbes[microbe][1] -= 1
            elif microbes[microbe][3] == 4:
                microbes[microbe][1] += 1

            # 미생물이 약품에 닿았는가?
            if microbes[microbe][0] == 0 or microbes[microbe][0] == N-1 or microbes[microbe][1] == 0 or microbes[microbe][1] == N-1:
                microbes[microbe][2] = microbes[microbe][2] // 2
                # 미생물 수를 절반으로 줄였으면 약품에 닿았으므로 이동 방향도 바꿔줌
                if microbes[microbe][3] == 1:
                    microbes[microbe][3] = 2
                elif microbes[microbe][3] == 2:
                    microbes[microbe][3] = 1
                elif microbes[microbe][3] == 3:
                    microbes[microbe][3] = 4
                elif microbes[microbe][3] == 4:
                    microbes[microbe][3] = 3

            # 두개 이상의 미생물의 좌표가 같은지 확인하기 위해 merge_list 확인
            location = [microbes[microbe][0], microbes[microbe][1]]  # 미생물 군집의 [x, y]좌표

            if location not in merge:
                merge.append(location)

        # 두개 이상의 미생물의 좌표가 같은지 따져보고 후처리
        for i in merge:  # i = [x, y]
            microbes_big = 0  # merge된 미생물 군집 중 더 큰 군집
            microbes_num = 0  # 더 큰 군집의 microbes내 idx
            microbes_sum = 0  # merge된 미생물 군집의 미생물 합
            temp_list = []

            for j in range(len(microbes)-1, -1, -1):  # range 범위 중요
                # 미생물 군집의 방향 찾기
                if [microbes[j][0], microbes[j][1]] == i:  # 좌표가 같고
                    if microbes[j][2] > microbes_big:  # 크기가 더 큰 군집 찾기
                        microbes_big = microbes[j][2]  # 더 큰 군집의 microbes내에서의 index 저장
                        microbes_num = j
                    temp_list.append(j)

            dir = microbes[microbes_num][3]

            for k in temp_list:
                pop_micro = microbes.pop(k)
                microbes_sum += pop_micro[2]

            # merge된 미생물 군집의 x,y 좌표, merge된 미생물 군집의 미생물 합, merge된 미생물 군집의 방향
            microbes.append([i[0], i[1], microbes_sum, dir])

    for microbe in microbes:
        answer += microbe[2]

    print(f'#{test_case} {answer}')