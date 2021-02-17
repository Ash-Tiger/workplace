S = input()
A=[]
for i in (97,123):
    if chr(i) in S:
        for j in range(len(S)):
            if chr(i) == S[j]:
                A.append(j)        
    else:
        A.append(-1)
print(A)

s = str(input())
digit = []
for i in range(ord('a'),ord('z')+1):
    digit.append(s.find(chr(i)))
print(digit)

for item in digit:
    print(item,end=" ")