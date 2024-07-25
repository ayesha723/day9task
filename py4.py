series=[1,2,3,3,4,5,5,6]

new_series=[]

for i in series:
    if i not in new_series:
        #append is a function through which we can add new inputs to the series
        new_series.append(i)

print("The new series excluding duplicates is " , new_series)




