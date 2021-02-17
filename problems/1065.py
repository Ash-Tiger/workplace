import sys

N = int(sys.stdin.readline())
num = 0

if N < 100:
    print(N)
else:
    num = 99
    for i in range(100,N+1):
        if (i//100-(i%100)//10) == ((i%100)//10-i%10) :
            num += 1
    print(num)
