numbers = [1,1,2,2,2,3,3,3,3,4,4,4,4,]
count_of_number = {}
for i in numbers:
    count_of_number[i]=count_of_number.get(i,0)+1
print (count_of_number)
