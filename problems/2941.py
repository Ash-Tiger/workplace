import sys

yo = sys.stdin.readline()

tt = len(yo)-1
 
tt -= yo.count('=')
tt -= yo.count('-')
tt -= yo.count('dz=')
tt -= yo.count('lj')
tt -= yo.count('nj')

print(tt)
