import sys

N = int(sys.stdin.readline())
i = 0

while True:import sys

N = int(sys.stdin.readline())
i = 0

while True:
    i += 1
    Summ = (1+i)*i/2
    if N <= Summ:
        seq = int(Summ - N)
        break

if i % 2 ==0:
    print(str(i-seq) +'/' + str(1+seq))
else:
    print(str(1+seq) +'/' + str(i-seq))   
    i += 1
    Summ = (1+i)*i/2
    if N <= Summ:
        seq = int(Summ - N)
        break

if i % 2 ==0:
    print(str(i-seq) +'/' + str(1+seq))
else:
    print(str(1+seq) +'/' + str(i-seq))   