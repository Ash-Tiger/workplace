import sys
a=int(5)
b=int(5)
while a > 0 and a < 10 and b>0 and b<10:
    a,b = map(int,sys.stdin.readline().split())
    print(a+b)
