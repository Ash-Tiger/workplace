import sys
A,B,C = map(int,sys.stdin.readline().split())

if  B >= C or A == 0:
    print(-1)
else:
    print(int((A/(C-B)))+1)