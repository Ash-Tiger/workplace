import sys

case_n = int(sys.stdin.readline())
case = [] 

for i in range(case_n):
    case.append(str(sys.stdin.readline()))
    score = 0
    add = 1
    
    for j in range(len(case[i])):
        if case[i][j] == 'O':
            score += add
            add += 1
        else:
            add = 1
    print(score)
