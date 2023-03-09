'''
1/1
2/1 1/2
3/1 2/2 1/3
4/1 3/2 2/3 1/4
5/1 4/2 3/3 2/4 1/5
6/1 5/2 4/3 3/4 2/5 1/6
7/1 6/2 5/3 4/4 3/5 2/6 1/7
'''

X = int(input())

line = 1  # 사선 라인

while X > line:  # 라인 위치 찾고 라인 위치에 X를 몇번째에 위치하는지 X에 저장
    X -= line
    line += 1

if line % 2 == 0:  # 짝수 라인업
    up = X  #
    down = line - X + 1
else:
    up = line - X + 1
    down = X

print(up,'/',down, sep="")
