num=int(input("Enter a number and find its fibbo series"))

fibo_series=0
for i in range(1 , num+1):
    fibo_series = fibo_series + i

print("The fibo series is " , fibo_series) # if put 4 the 0+1+2+3+4 = 10