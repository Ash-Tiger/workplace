import sys

case_num = int(sys.stdin.readline())

for i in range(case_num):
    H,W,N = map(int,sys.stdin.readline().split()) 
    print('%d%02d' %(((N-1)%H+1),((N-1)//H)+1))