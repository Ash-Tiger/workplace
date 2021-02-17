import sys
n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))

M = max(a)
T=0
for i in a:
    T = T + (i/M)*100

print(T/n)