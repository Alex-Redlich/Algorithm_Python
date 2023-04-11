while True:
    a, b, c = map(int,input().split())
    if a == 0 and b == 0 and c ==0 :
        break
    num = []
    num.append(a)
    num.append(b)
    num.append(c)
    num.sort(reverse=True)
    if num[0]**2 == num[1]**2 + num[2]**2 :
        print('right')
    else:
        print('wrong')