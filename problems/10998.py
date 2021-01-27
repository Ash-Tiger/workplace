a=int(input())
b=int(input())

c3 = a*(b%10)
print(c3)

c4 = int(a*(b%100/10))
print(c4)

c5 = a*int(b/100)
print(c5)

print(a*b)