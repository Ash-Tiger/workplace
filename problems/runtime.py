import timeit
sum=0
for i in range(10):
    sum +=i
st=timeit.default_timer()
print(f"the result is {sum}and {sum}{sum}{sum}this calculate tooks")
tt=timeit.default_timer()
print(tt-st)
st=timeit.default_timer()
print("the result is %d and %d %d %d this calculate tooks" % (sum,sum,sum,sum))
tt=timeit.default_timer()
print(tt-st)
st=timeit.default_timer()
print("the result is",sum,"and ",sum,sum,sum,"this calculate tooks")
tt=timeit.default_timer()
print(tt-st)
