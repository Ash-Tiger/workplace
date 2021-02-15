import sys

n = sys.stdin.read()
a = list(map(int,sys.stdin.read()))

print(n, a)

for i in range(a):
    if maxx > i:
        
    else:
        maxx=i

for i in range(a):
    if minn >i:
        minn = i

print(maxx, minn)