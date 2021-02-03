import sys

a=c=int(sys.stdin.readline())
t = 0

while True:
    a = int(str(a%10)+str((a//10+a%10)%10))
    t += 1
    if a==c:
        print(t)
        break