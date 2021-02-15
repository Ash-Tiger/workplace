import sys

n = sys.stdin.readline()
a = list(map(int,sys.stdin.readline().split()))

maxx = a[0]
minn = a[0]
for i in a:
    if maxx < i:
        maxx=i

for i in a:
    if minn >i:
        minn = i

print(minn, maxx)