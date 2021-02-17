import sys

N = int(sys.stdin.readline())
num = sys.stdin.readline().rstrip()

totalsum=0

for i in num:
    totalsum += int(i)

print(totalsum)