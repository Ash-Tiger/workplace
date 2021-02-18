S = input()
A=[]
for i in range(97,123,1):
    if chr(i) in S:
        A.append(S.find(chr(i)))   
    else:
        A.append(-1)
for j in A:
    print(j, end=' ')
