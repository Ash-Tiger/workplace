import sys

n = int(sys.stdin.readline())
a = int(1)
i = int(2)
b =  int(0)

while True:
    if n > a:
        a = 1+3*(i-1)*i
        b += 1
        i += 1
    else:
        b += 1
        print(b)
        break


'''
1 7 19 37 61
0 6 12 18 24 30 36 42
'''