import sys

num = sys.stdin.readline()

ttime = 0
for i in num:
    if i in 'ABC':
        ttime += 3
    elif i in 'DEF':
        ttime += 4
    elif i in 'GHI':
        ttime += 5
    elif i in 'JKL':
        ttime += 6
    elif i in 'MNO':
        ttime += 7
    elif i in 'PQRS':
        ttime += 8
    elif i in 'TUV':
        ttime += 9
    elif i in 'WXYZ':
        ttime += 10

print(ttime)
       
