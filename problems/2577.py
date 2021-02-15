import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

t = str(a*b*c)


for j in range(10):
    print(t.count(str(j)))

'''
w=[]
w.extend(t)
for i in range(10):
    z=int(0)
    for r in w:
        if i == int(r):
            z += 1
    print(z)
'''