import sys
from collections import Counter

q=[]
for i in range(10):
    q.append(int(sys.stdin.readline())%42)
print(len(Counter(q)))
print(len(q))

print(set(q))


