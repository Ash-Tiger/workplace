B = []
C = []
for i in range(1,10001):
    A = []
    A.extend(str(i))
    nonselnum = 0 
    for j in A:
        nonselnum += int(j)
    B.append(nonselnum+i)
    if nonselnum+i > 20000:
        break
    
for k in range(1,10001):
    if k in B:
        C.append(k)
    else:
        print(k)
