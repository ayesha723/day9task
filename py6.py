num=int(input ("Enter the number and i will first find square of the series like 5= 1sq + 2sq +.... and add them:"))

square_sum=0

for i in range (1 , num+1):
    square = i**2
    square_sum = square_sum +square

print("The sum of squares of series numbers of given number is ", square_sum)