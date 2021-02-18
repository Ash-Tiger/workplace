import sys

case_num = int(sys.stdin.readline())

for i in range(case_num):
    R, S = sys.stdin.readline().split()
    SS=''
    for j in S:
        SS += str(j*int(R))
    print(SS)    