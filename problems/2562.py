import sys

a = []
for i in range(9):
    t =int(sys.stdin.readline())
    a.append(t)

print(max(a))
print(a.index(max(a))+1)