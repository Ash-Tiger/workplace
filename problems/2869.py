import sys
import math

A,B,V= map(int,sys.stdin.readline().split())

#print(math.ceil((V-A)/(A-B))+1)
print(int((V-A)/(A-B)+0.99)+1)