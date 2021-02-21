import sys

case_n = int(sys.stdin.readline())

for i in range(case_n):
    case = list(map(int,sys.stdin.readline().split()))
    mean = (sum(case) - case[0])/case[0]
    num = 0
    for j in case[1:]:
        if j > mean:
            num += 1
    ans = ((num/case[0]) * 100)
    print('%.3f' % ans +'%') # <<< 표현하는 방법 궁금