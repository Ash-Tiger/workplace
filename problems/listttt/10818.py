import sys

n = sys.stdin.read()
a = map(int,list(sys.stdin.read()))


for i in range(n):
    for t in range(i+1,n):
        if a[t] >=a[i]:
            maxx = max
        else:
            max = a[i]    




            min = a[i]
