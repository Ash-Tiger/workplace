import sys

S = sys.stdin.readline().upper()
A=[]

for i in range(65,91,1):
    A.append(S.count(chr(i)))

if  A.count(max(A))>= 2:
    print('?')
else:
    print(chr(65+A.index(max(A))))
