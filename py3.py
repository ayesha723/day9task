series= '123456'

#first digit comes in index 
largest_num=int(series[0]) #1 

for digit in series: # 123456
    current_num= int(digit) 
    
    if current_num>largest_num: 
        #largest is updated in each iteration
        #2>1 3>2 4>3 5>4 6>5 
        largest_num = current_num
        
print("The largert number in series is " ,+largest_num)

#for smallest number in series
smallest_num=int (series[0])
for digit in series:
    current_num=int(digit)
    if current_num < smallest_num:
        smallest_num = current_num
print("The smallest number in series is " ,+smallest_num)