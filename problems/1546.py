a = int(input())
for i in range(1,a+1):
    print(' '*(a-i)+'*'*(i))

print('abc','cdf') # , 로 구분하면 , 부분은 공백 처리
print('abc'+'cdf') # +로 구문하면 + 사이 공백없이 연결됨
