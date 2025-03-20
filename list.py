numbers = [1,1,1,1,1,6,2,2,2,3,3,3,4,4,5]

count_of_numbers = {}


for i in numbers:
    if i in count_of_numbers:
       count_of_numbers[i]+=1
    else:
       count_of_numbers[i]=1
print(count_of_numbers)
